"""Transforma los cubos de MecaU en geometría que entienden GLB y OBJ."""

from pathlib import Path
import trimesh
from trimesh.visual.material import PBRMaterial

# Las seis caras de un cubo: cada cara se dibuja con 2 triángulos.
# Cada entrada indica: dirección del vecino, y las cuatro esquinas de esa cara.
FACES = [
    (( 1, 0, 0), [(1,0,0), (1,1,0), (1,1,1), (1,0,1)]),  # derecha
    ((-1, 0, 0), [(0,0,0), (0,0,1), (0,1,1), (0,1,0)]),  # izquierda
    (( 0, 1, 0), [(0,1,0), (0,1,1), (1,1,1), (1,1,0)]),  # arriba
    (( 0,-1, 0), [(0,0,0), (1,0,0), (1,0,1), (0,0,1)]),  # abajo
    (( 0, 0, 1), [(0,0,1), (1,0,1), (1,1,1), (0,1,1)]),  # delante
    (( 0, 0,-1), [(0,0,0), (0,1,0), (1,1,0), (1,0,0)]),  # detrás
]


def make_meshes(model):
    """Agrupa por color las caras visibles y forma una malla para cada color."""
    meshes = {}   # color -> listas de vertices y triangulos

    for (x, y, z), color in model.voxels.items():
        vertices, triangles = meshes.setdefault(color, ([], []))

        for (nx, ny, nz), corners in FACES:
            # Si hay otro cubo al lado, no dibujamos esa cara interna.
            if (x + nx, y + ny, z + nz) in model.voxels:
                continue

            index = len(vertices)
            for dx, dy, dz in corners:
                vertices.append((x + dx, y + dy, z + dz))

            triangles.append((index, index + 1, index + 2))
            triangles.append((index, index + 2, index + 3))

    return meshes


def save_model(model, filename: Path):
    """Escribe GLB (único archivo) u OBJ acompañado de un archivo MTL."""
    if not model.voxels:
        raise ValueError("El modelo está vacío: añade al menos un voxel")
    ext = filename.suffix.lower()
    if ext not in (".glb", ".obj"):
        raise ValueError("Solo se puede exportar a .glb o .obj")

    filename.parent.mkdir(parents=True, exist_ok=True)
    meshes = make_meshes(model)

    if ext == ".glb":
        scene = trimesh.Scene()
        for color, (vertices, triangles) in meshes.items():
            if not triangles:
                continue
            mesh = trimesh.Trimesh(vertices=vertices, faces=triangles, process=False)
            rgb = [int(color[i:i+2], 16) for i in (1, 3, 5)]
            mesh.visual = trimesh.visual.TextureVisuals(
                material=PBRMaterial(
                    name="color_" + color[1:],
                    baseColorFactor=rgb + [255],
                    metallicFactor=0,
                    roughnessFactor=1,
                )
            )
            scene.add_geometry(mesh, geom_name="voxels_" + color[1:])
        scene.export(str(filename), file_type="glb")

    else:
        # OBJ guarda la forma, mientras que MTL guarda los colores.
        lines = ["# OBJ generado por MecaU", "mtllib " + filename.with_suffix(".mtl").name]
        mtl = ["# Materiales de MecaU"]
        start = 1  # En OBJ los índices empiezan en 1.

        for color, (vertices, triangles) in meshes.items():
            material_name = "color_" + color[1:]
            rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
            mtl += [f"newmtl {material_name}",
                    f"Kd {rgb[0]:.6f} {rgb[1]:.6f} {rgb[2]:.6f}", ""]
            if not triangles:
                continue
            lines += ["o " + material_name, "usemtl " + material_name]
            for x, y, z in vertices:
                lines.append(f"v {x} {y} {z}")
            for a, b, c in triangles:
                lines.append(f"f {start+a} {start+b} {start+c}")
            start += len(vertices)

        filename.write_text("\n".join(lines) + "\n", encoding="utf-8")
        filename.with_suffix(".mtl").write_text("\n".join(mtl) + "\n", encoding="utf-8")

    return filename

