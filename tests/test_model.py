from mecau import VoxelModel
from mecau.export import make_meshes
import trimesh
import pytest


def test_one_voxel():
    m = VoxelModel()
    m.voxel(0, 0, 0, "#FF0000")
    assert m.voxels[(0, 0, 0)] == "#FF0000"
    vs, triangles = make_meshes(m)["#FF0000"]
    assert len(vs) == 24
    assert len(triangles) == 12


def test_two_voxels_do_not_export_shared_faces():
    m = VoxelModel()
    m.box(0, 0, 0, 2, 1, 1)
    vs, triangles = make_meshes(m)["#FFFFFF"]
    assert len(triangles) == 20  # 10 caras visibles


def test_export(tmp_path):
    m = VoxelModel()
    m.voxel(0, 0, 0, "#0088FF")
    glb = m.export(tmp_path / "prueba.glb")
    assert glb.read_bytes()[:4] == b"glTF"
    assert len(trimesh.load(str(glb), force="scene").geometry) == 1


def test_bad_inputs(tmp_path):
    m = VoxelModel()
    with pytest.raises(ValueError):
        m.voxel(0.5, 1, 2)
    with pytest.raises(ValueError):
        m.box(0, 0, 0, -1, 2, 2)
    with pytest.raises(ValueError):
        m.voxel(0, 0, 0, "rojo")
    m.voxel(0, 0, 0)
    with pytest.raises(ValueError, match=r"Solo se puede exportar a \.glb"):
        m.export(tmp_path / "prueba.obj")
    with pytest.raises(ValueError, match=r"Solo se puede exportar a \.glb"):
        m.export("test.ply")

