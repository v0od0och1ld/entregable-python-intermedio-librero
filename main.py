from view import main_loop
from model import *


try:
    conexion()
    crear_tabla_libros()    
except:
    print("Hay un error en la creación de la tabla de libros o la misma ya fue creada anteriormente")


try:
    conexion()
    crear_tabla_categorias()    
except:
    print("Hay un error en la creación de la tabla de categorias o la misma ya fue creada anteriormente")

try:
    conexion()
    agregar_generos_literarios()    
except:
    print("Hay un error en el agregado de los géneros literarios o los mismos ya fueron creados anteriormente")

try:
    conexion()
    crear_tabla_autores()    
except:
    print("Hay un error en la creación de la tabla de autores o la misma ya fue creada anteriormente")    

try:
    conexion()
    agregar_autores()    
except:
    print("Hay un error en el agregado de autores o los mismos ya fueron creados anteriormente")

try:
    conexion()
    crear_tabla_editorial()    
except:
    print("Hay un error en la creación de la tabla de editoriales o la misma ya fue creada anteriormente")

try:
    conexion()
    agregar_editoriales()    
except:
    print("Hay un error en el agregado de las editoriales o las mismos ya fueron creados anteriormente")


    










    

main_loop()




