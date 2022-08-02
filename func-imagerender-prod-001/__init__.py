import sys
import logging
import subprocess

# import cadquery as cq

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    res = subprocess.call("blender --background --python func-imagerender-prod-001/script.py") #--background 
    
    # res = subprocess.call("freecad func-imagerender-prod-001/script_2.py")

    logging.info(f"Result: {res}")

    return func.HttpResponse(
        "Done",
        status_code=200
    )
