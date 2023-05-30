import numpy as np
import open3d as o3d
import os


class params():
    # voxels counter that will stop the voxel mesh generation when there are no more voxels in the voxel grid
    counter = 0
    vox_mesh=o3d.geometry.TriangleMesh()

# Voxel builder callback function
def build_voxels(vis):
    # check if the counter is more than the amount of voxels
    if params.counter < len(voxels_all):
        # get the size of the voxels
        voxel_size = voxel_grid.voxel_size
        # create a box primitive of size 1x1x1
        cube=o3d.geometry.TriangleMesh.create_box(width=1, height=1, depth=1)
        # paint the box uniformly with the color of the voxel
        cube.paint_uniform_color(voxels_all[params.counter].color)
        # scale the box to the size of the voxel
        cube.scale(voxel_size, center=cube.get_center())
        # get the center position of the current voxel
        voxel_center = voxel_grid.get_voxel_center_coordinate(voxels_all[params.counter].grid_index)
        # translate the box to the voxel center
        cube.translate(voxel_center, relative=False)
        # add the box primitive to the voxel mesh
        params.vox_mesh+=cube
        
        # on the first loop create the geometry and on subsequent iterations update the geometry
        if params.counter==0:
            vis.add_geometry(params.vox_mesh)
        else:
            vis.update_geometry(params.vox_mesh)

        # update the renderer
        vis.update_renderer()
        # tick up the counter
        params.counter+=1
        
        
        
mesh_path = os.path.join('taxi', 'taxi.obj')
mesh = o3d.io.read_triangle_mesh(mesh_path, True)

print(mesh)
print("Vertices:")
print(np.asarray(mesh.vertices))
print("Triangles:")
print(np.asarray(mesh.triangles))

mesh_faces = mesh.triangles
mesh_uvs = mesh.triangle_uvs
texture = mesh.textures


vis.create_window(window_name='Something Visualize', width = 800, height = 600)

vis.add_geometry(mesh)
