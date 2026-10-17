"""El corazón de MecaU: guardar cubos en una cuadrícula 3D."""

from pathlib import Path


class VoxelModel:
    def __init__(self, name="Modelo"):
        self.name = name
        # Clave = (x, y, z). Valor = color hexadecimal, como "#FF0000".
        self.voxels = {}

    def voxel(self, x, y, z, color="#FFFFFF"):
        """Coloca UN cubo de tamaño 1 en una posición entera."""
        if any(type(n) is not int for n in (x, y, z)):
            raise ValueError("Las coordenadas deben ser números enteros")
        if not isinstance(color, str) or len(color) != 7 or not color.startswith("#"):
            raise ValueError("El color debe tener el formato #RRGGBB")
        try:
            int(color[1:], 16)
        except ValueError as error:
            raise ValueError("El color debe tener el formato #RRGGBB") from error

        self.voxels[(x, y, z)] = color.upper()
        return self

    def box(self, x, y, z, width, height, depth, color="#FFFFFF"):
        """Crea una caja colocando varios cubos de tamaño 1."""
        if any(type(n) is not int or n <= 0 for n in (width, height, depth)):
            raise ValueError("Las dimensiones deben ser enteros positivos")

        for dx in range(width):
            for dy in range(height):
                for dz in range(depth):
                    self.voxel(x + dx, y + dy, z + dz, color)
        return self

    def export(self, filename):
        """Convierte los cubos guardados en un archivo .glb o .obj."""
        from .export import save_model
        return save_model(self, Path(filename))

