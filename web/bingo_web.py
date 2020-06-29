from jinja2 import Template
import os
import sys
sys.path.append(os.getcwd())
from src.bingo import carton

template = Template(open("web/plantilla.j2").read())

file = open("web/bingo.html", "w")
file.write(template.render(carton = carton()))
file.close()

print("Abrir el archivo bingo.html para ver el carton")
