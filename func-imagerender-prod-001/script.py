import logging

import bpy
import os
import math

from math import *
from mathutils import Vector

from bpy import context

print('Inside script file')

# Open folder
cwd = os.getcwd()
os.chdir('func-imagerender-prod-001')

# Check for input and output files
cwd = os.getcwd()

for folder in ["input", "dataset"]:
    if not os.path.exists(folder):
        os.mkdir(folder)


# # Open images
os.chdir('input')

# # Get all stp files
cwd = os.getcwd()

for file_nr, stl_file in enumerate(os.listdir(cwd)):

    # Determine bpy settings
    bpy.context.scene.render.use_compositing = True
    bpy.context.scene.use_nodes = True
    bpy.context.scene.render.resolution_x = 2000
    bpy.context.scene.render.resolution_y = 2000

    cam = bpy.context.scene.camera
    cam.data.show_background_images = True
    cam.rotation_mode = 'XYZ'
    cam.data.clip_end = 1000
    cam.rotation_euler = (math.radians(0), math.radians(0), math.radians(90))
    
    for o in bpy.context.scene.objects:
        print("Object name: {}".format(o.name))
        if o.name == "Cube" or o.name.startswith("DOC"):
            bpy.ops.object.delete(use_global=False)

    bpy.ops.import_mesh.stl(filepath = stl_file)
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')  

    for x_angle in range(0, 361, 45):
        for y_angle in range(0, 361, 45):
            for z_angle in range(0, 361, 45):
                obj = bpy.context.object
                obj.location = Vector((0.0, 0.0, 0.0))
                obj.rotation_euler = (math.radians(x_angle), math.radians(y_angle), math.radians(z_angle))

                filename = stl_file.replace('.stl', '').split("-")[1].rstrip()
                data_filename = str(filename) + '_' + str(file_nr) + '_' + str(x_angle) + '_' + str(y_angle) + '_' + str(z_angle) + '.png'
                data_save_path = os.path.join("C:/Users/hedak/PycharmProjects/NooteboomAI/func-imagerender-prod-001/dataset", data_filename)
                
                bpy.ops.view3d.camera_to_view_selected()
                bpy.context.scene.render.film_transparent = True
                bpy.context.scene.camera = cam
                bpy.context.scene.render.filepath = data_save_path
                bpy.context.scene.render.image_settings.color_mode = 'RGBA' 
                bpy.ops.render.render(write_still = True)


print('Done script file')