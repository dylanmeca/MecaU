"""Ejercicio inicial: una casita voxel con paredes, techo y puerta."""

from pathlib import Path
from mecau import VoxelModel

casa = VoxelModel("Mi casa")

# 1. Base de piedra
casa.box(0, 0, 0, 10, 1, 8, "#777777")

# 2. Paredes (dejamos el interior vacío)
for y in range(1, 6):
    for x in range(10):
        casa.voxel(x, y, 0, "#E5D7B8")
        casa.voxel(x, y, 7, "#E5D7B8")
    for z in range(8):
        casa.voxel(0, y, z, "#E5D7B8")
        casa.voxel(9, y, z, "#E5D7B8")

# 3. Puerta oscura en la pared frontal
for y in range(1, 4):
    for x in (4, 5):
        casa.voxel(x, y, 0, "#443322")

# 4. Techo plano
casa.box(0, 6, 0, 10, 1, 8, "#8B3434")

# 5. Guarda el modelo en la carpeta donde está este ejemplo
out = Path(__file__).parent
casa.export(out / "casa.glb")
print("¡Casa creada! Voxels:", len(casa.voxels))

