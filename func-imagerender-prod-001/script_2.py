import Mesh
import Part
import FreeCAD
import os

list_dir = os.listdir("C:/cad_input")

for file_name in list_dir:
    input_path = f"C:/cad_input/{file_name}"
    mod_file_name = file_name.replace('.ipt.stp', '.stl')
    shape=Part.Shape()
    shape.read(input_path)
    shape.exportStl(f"C:/cad_output/{mod_file_name}")
