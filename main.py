
#from model import agregar_autores, agregar_editoriales, agregar_generos_literarios, conexion, crear_tabla_autores, crear_tabla_categorias, crear_tabla_editorial, crear_tabla_libros
#from view import main_loop
from model import Base
from view import Ventana


try:
    conn = Base.conexion()
    conn.crear_tabla_libros()    
except:
    print("Hay un error en la creación de la tabla de libros o la misma ya fue creada anteriormente")


try:
    conn = Base.conexion()
    conn.crear_tabla_categorias()
except:
    print("Hay un error en la creación de la tabla de categorias o la misma ya fue creada anteriormente")

try:
    conn = Base.conexion()
    conn.agregar_generos_literarios()
except:
    print("Hay un error en el agregado de los géneros literarios o los mismos ya fueron creados anteriormente")

try:
    conn = Base.conexion()
    conn.crear_tabla_autores()
except:
    print("Hay un error en la creación de la tabla de autores o la misma ya fue creada anteriormente")    

try:
    conn = Base.conexion()
    conn.agregar_autores()
except:
    print("Hay un error en el agregado de autores o los mismos ya fueron creados anteriormente")

try:
    conn = Base.conexion()
    conn.crear_tabla_editorial()
except:
    print("Hay un error en la creación de la tabla de editoriales o la misma ya fue creada anteriormente")

try:
    conn = Base.conexion()
    conn.agregar_editoriales()    
except:
    print("Hay un error en el agregado de las editoriales o las mismos ya fueron creados anteriormente")

ventana = Ventana()
ventana.main_loop()
