import sqlite3
import tkinter as tk

class Base:

    def __init__(self,):
        pass
    
    @staticmethod
    def conexion():
        conn = sqlite3.connect("base_librero.db")
        return conn


    @staticmethod
    def cargar_libros(tree):    

        conn = Base.conexion()
        cursor = conn.cursor()

        sql = """
            SELECT l.id, l.titulo, a.autor, e.editorial, l.anio, c.categoria, l.comentario
            FROM libros AS l 
            INNER JOIN autores AS a ON a.id = l.autor 
            INNER JOIN editoriales AS e ON e.id = l.editorial
            INNER JOIN categorias AS c ON c.id = l.categoria
        """

        try:
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                tree.insert("", tk.END, values=row)
        except:
            pass

    @staticmethod    
    def crear_tabla_libros():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = """CREATE TABLE libros
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo varchar(255) NOT NULL,
                autor integer,
                editorial integer,
                anio integer,
                categoria integer,
                comentario varchar(255))
        """
        cursor.execute(sql)
        conn.commit()
        
    @staticmethod
    def crear_tabla_categorias():   
        conn = Base.conexion()
        cursor = conn.cursor() 
        sql1 = """CREATE TABLE categorias
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                categoria varchar(255) NOT NULL)
        """
        cursor.execute(sql1)
        conn.commit()
    
    @staticmethod
    def agregar_generos_literarios():
        conn = Base.conexion()
        cursor = conn.cursor()

        generos = ["Novela", "Poesía", "Drama", "Ensayo", "Ciencia ficción", "Fantasía", "Misterio", "Terror", "Aventura"]

        cursor.execute("SELECT categoria FROM categorias")
        categorias_existentes = cursor.fetchall()
        categorias_existentes = [cat[0] for cat in categorias_existentes]
            
        for genero in generos:
            if genero not in categorias_existentes:
                sql = "INSERT INTO categorias (categoria) VALUES (?)"
                cursor.execute(sql, (genero,))
        
        conn.commit()

    @staticmethod
    def agregar_editoriales():
        conn = Base.conexion()
        cursor = conn.cursor()

        editoriales = ["Planeta", "Sudamericana", "Siglo XXI Editores", "Paidós", "Interzona", "Emece", "El Ateneo", "Galerna", "Adriana Hidalgo", "Ediciones Continente"]

        cursor.execute("SELECT editorial FROM editoriales")
        editoriales_existentes = cursor.fetchall()
        editoriales_existentes = [edito[0] for edito in editoriales_existentes]
            
        for editorial in editoriales:
            if editorial not in editoriales_existentes:
                sql = "INSERT INTO editoriales (editorial) VALUES (?)"
                cursor.execute(sql, (editorial,))
        
        conn.commit()

    @staticmethod
    def crear_tabla_autores():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = """CREATE TABLE autores
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                autor varchar(50))
        """
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def crear_tabla_editorial():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = """CREATE TABLE editoriales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                editorial varchar(50))
        """
        cursor.execute(sql)
        conn.commit()

    @staticmethod
    def agregar_autores():
        conn = Base.conexion()
        cursor = conn.cursor()

        autores = ["Jorge Luis Borges", "Julio Cortázar", "Adolfo Bioy Casares", "Ernesto Sabato", "Marta Lynch", "Leopoldo Marechal"]

        cursor.execute("SELECT autor FROM autores")
        autores_existentes = cursor.fetchall()
        autores_existentes = [aut[0] for aut in autores_existentes]
            
        for autor in autores:
            if autor not in autores_existentes:
                sql = "INSERT INTO autores (autor) VALUES (?)"
                cursor.execute(sql, (autor,))
        
        conn.commit()

    def buscar_categoria(self, nombre_categoria):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM categorias WHERE categoria = ?"

        cursor.execute(sql, (nombre_categoria,))
        resultado = cursor.fetchone()

        return resultado
    
    @staticmethod
    def buscar_categorias():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM categorias order by categoria asc"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        categorias_formateadas = [f"{categoria[0]} {categoria[1]}" for categoria in resultado] #CAMBIAR

        return categorias_formateadas
    
    
    
    # Graba en la bd la nueva categoria
    def guardar_categoria(self, nombre_categoria):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO categorias (categoria) VALUES(?)"
        try:
            cursor.execute(sql, (nombre_categoria,))
            print(f"Categoría guardada: {nombre_categoria}")
        except:
            print(f"Error al guardar la Categoría {nombre_categoria}")
        conn.commit()


    def guardar_mod_categoria(self, nombre, categoriamod):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "UPDATE categorias SET categoria = ? WHERE categoria = ?"
        try:       
            cursor.execute(sql, (categoriamod, nombre))
            conn.commit()
            
            return 1        
        except:
            conn.close()  

    def borrar_categoria(self, nombre):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM categorias WHERE categoria = ?"
            
        try:       
            cursor.execute(sql, (nombre,))
            conn.commit()
            conn.close()        
            return 1        
        except:
            conn.close()  



    def buscar_editorial(self, nombre_editorial):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM editoriales WHERE editorial = ?"

        cursor.execute(sql, (nombre_editorial,))
        resultado = cursor.fetchone()

        return resultado

    @staticmethod
    def buscar_editoriales():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM editoriales order by editorial asc"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        editoriales_formateadas = [f"{editorial[0]} {editorial[1]}" for editorial in resultado] #CAMBIAR

        return editoriales_formateadas
    
    
    
    # Graba en la bd la nueva editorial
    def guardar_editorial(self, nombre_editorial):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO editoriales (editorial) VALUES(?)"
        try:
            cursor.execute(sql, (nombre_editorial,))
            print(f"Categoría guardada: {nombre_editorial}")
        except:
            print(f"Error al guardar la editorial {nombre_editorial}")
        conn.commit()


    def guardar_mod_editorial(self, nombre, editorialmod):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "UPDATE editoriales SET editorial = ? WHERE editorial = ?"
        try:       
            cursor.execute(sql, (editorialmod, nombre))
            conn.commit()
            
            return 1        
        except:
            conn.close()  


    def borrar_editorial(self, nombre):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM editoriales WHERE editorial = ?"
            
        try:       
            cursor.execute(sql, (nombre,))
            conn.commit()
            conn.close()        
            return 1        
        except:
            conn.close()  

    def buscar_autor(self, nombre_autor):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM autores WHERE autor = ?"

        cursor.execute(sql, (nombre_autor,))
        resultado = cursor.fetchone()

        return resultado
    @staticmethod
    def buscar_autores():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM autores order by autor asc"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        autores_formateados = [f"{autor[0]} {autor[1]}" for autor in resultado] #CAMBIAR
        

        return autores_formateados #CAMBIAR EN LOS OTROS CRUD
    
    
    
    # Graba en la bd el nuevo autor
    def guardar_autor(self, nombre_autor):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "INSERT INTO autores (autor) VALUES(?)"
        try:
            cursor.execute(sql, (nombre_autor,))
            print(f"Autor guardado: {nombre_autor}")
        except:
            print(f"Error al guardar el autor {nombre_autor}")
        conn.commit()


    def guardar_mod_autor(self, nombre, autormod):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "UPDATE autores SET autor = ? WHERE autor = ?"
        try:       
            cursor.execute(sql, (autormod, nombre))
            conn.commit()
            
            return 1        
        except:
            conn.close()  


    def borrar_autor(self, nombre):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM autores WHERE autor = ?"
            
        try:       
            cursor.execute(sql, (nombre,))
            conn.commit()
            conn.close()        
            return 1        
        except:
            conn.close()  


    def buscar_libro(self, nombre_libro):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM libros WHERE titulo = ?"

        #0 id
        #1 titulo
        #2 autor
        #3 editorial
        #4 anio
        #5 categoria
        #6 comentario

        cursor.execute(sql, (nombre_libro,))
        resultado = cursor.fetchone()

        return resultado

    @staticmethod
    def buscar_libros():
        conn = Base.conexion()
        cursor = conn.cursor()
        sql = "SELECT * FROM libros order by libro asc"

        cursor.execute(sql)
        resultado = cursor.fetchall()

        libros_formateados = [f"{libro[0]} {libro[1]}" for libro in resultado] #CAMBIAR

        return libros_formateados

    def obtener_id_autor(self, autor):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT id FROM autores WHERE autor = ?"
        
        cursor.execute(sql, (autor,))
        resultado = cursor.fetchone()

        return resultado    

    def obtener_id_editorial(self, editorial):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT id FROM editoriales WHERE editorial = ?"
        
        cursor.execute(sql, (editorial,))
        resultado = cursor.fetchone()

        return resultado    

    def obtener_id_categoria(self, categoria):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "SELECT id FROM categorias WHERE categoria = ?"
        
        cursor.execute(sql, (categoria,))
        resultado = cursor.fetchone()

        return resultado    
    
    # Graba en la bd el nuevo libro
    def guardar_libro(self, nombre_libro, autor, editorial, anio, genero, comentario):
        indice_espacio_autor = autor.find(' ')
        autor_sin_numero = autor[indice_espacio_autor + 1:]        
        autor_id = self.obtener_id_autor(autor_sin_numero)

        indice_espacio_editorial = editorial.find(' ')
        editorial_sin_numero = editorial[indice_espacio_editorial + 1:]        
        editorial_id = self.obtener_id_editorial(editorial_sin_numero)
        
        
        indice_espacio_genero = genero.find(' ')
        genero_sin_numero = genero[indice_espacio_genero + 1:] 
        genero_id = self.obtener_id_categoria(genero_sin_numero)


        conn = self.conexion()
        cursor = conn.cursor()

        #sql = "INSERT INTO libros (titulo, autor, editorial, anio, categoria, comentario) VALUES(?, ?, ?, ?, ?, ?)" 

        sql = ("""INSERT INTO libros (titulo, autor, editorial, anio, categoria, comentario) 
                    VALUES ('{}',{}, {}, {},{},'{}')""".format(nombre_libro, autor_id[0], editorial_id[0], anio, genero_id[0], comentario))
                    


        try:
            #cursor.execute(sql, (nombre_libro, autor_id[0], editorial_id[0], anio, genero_id[0], comentario))
            cursor.execute(sql)
            conn.commit()

            print(f"Libro guardado: {nombre_libro}")
        except Exception as e:
            print(f"Error al guardar el libro {nombre_libro}: {e}")
            conn.rollback() 
        finally:
            conn.close()  


    def guardar_mod_libro(self, nombre, libromod):
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "UPDATE libros SET libro = ? WHERE libro = ?"
        try:       
            cursor.execute(sql, (libromod, nombre))
            conn.commit()
            
            return 1        
        except:
            conn.close()  


    def eliminar_libro_db(self, libro_id):
        
        conn = self.conexion()
        cursor = conn.cursor()
        sql = "DELETE FROM libros WHERE id = ?"

        try:
            cursor.execute(sql, (libro_id,))
            conn.commit()
            conn.close()
            return True
        except:
            conn.close()
            return False