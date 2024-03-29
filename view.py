from tkinter import *
from tkinter.messagebox import *
from tkinter import Tk, ttk

import re

#from model import borrar_autor, borrar_categoria, borrar_editorial, buscar_autor, buscar_autores, buscar_categoria, buscar_categorias, buscar_editorial, buscar_editoriales, buscar_libro, cargar_libros, eliminar_libro_db, guardar_autor, guardar_categoria, guardar_editorial, guardar_libro, guardar_mod_autor, guardar_mod_categoria, guardar_mod_editorial
from model import Base

class Ventana:

    def __init__(self,):
        #root = None #la declaro afuera para luego declararla global dentro del main loop para que la pueda tomar en el resto de las ventanas
        #tree = None
        self.root = None
        #self.tree = ttk.Treeview(self.root)
        self.tree = None


    def limpiar_treeview(self,):
        # Eliminar todos los elementos del Treeview
        if self.tree:
            for item in self.tree.get_children():
                self.tree.delete(item)

    def main_loop(self,):
        #global root, tree #la declaro global para poder referenciarla luego desde otras ventanas
        self.root = Tk()
        self.root.title("Librero")
        base = Base()

        menubar = Menu(self.root) #Menu

        menu_archivo = Menu(menubar, tearoff=0) #tearoff es para subniveles de menu

        #Libros
        submenu_libros = Menu(menu_archivo, tearoff=0)
        submenu_libros.add_command(label="Nuevo", command=self.nuevo_libro)
        #submenu_libros.add_command(label="Modificar", command=modificar_libro)
        submenu_libros.add_command(label="Eliminar", command=self.eliminar_libro)
        menu_archivo.add_cascade(label="Libros", menu=submenu_libros)
        #Libros

        #Categorias
        submenu_categorias = Menu(menu_archivo, tearoff=0)
        submenu_categorias.add_command(label="Nueva Categoría", command=self.nueva_categoria)
        submenu_categorias.add_command(label="Modificar Categoría", command=self.modificar_categoria)
        submenu_categorias.add_command(label="Eliminar Categoría", command=self.eliminar_categoria)
        menu_archivo.add_cascade(label="Categorías", menu=submenu_categorias)
        #Categorias

        #Editoriales
        submenu_editoriales = Menu(menu_archivo, tearoff=0)
        submenu_editoriales.add_command(label="Nueva Editorial", command=self.nueva_editorial)
        submenu_editoriales.add_command(label="Modificar Editorial", command=self.modificar_editorial)
        submenu_editoriales.add_command(label="Eliminar Editorial", command=self.eliminar_editorial)
        menu_archivo.add_cascade(label="Editoriales", menu=submenu_editoriales)
        #Editoriales

        #Autores
        submenu_autores = Menu(menu_archivo, tearoff=0)
        submenu_autores.add_command(label="Nuevo Autor", command=self.nuevo_autor)
        submenu_autores.add_command(label="Modificar Autor", command=self.modificar_autor)
        submenu_autores.add_command(label="Eliminar Autor", command=self.eliminar_autor)
        menu_archivo.add_cascade(label="Autores", menu=submenu_autores)
        #Autores

        menu_archivo.add_separator()

        menu_archivo.add_command(label="Salir", command=self.root.quit)

        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        self.root.config(menu=menubar)

        ##### ESTE ES EL TREEVIEW

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("id","titulo","autor","editorial","anio","categoria","comentario")
        #tree.column("#0", width=50, minwidth=50, anchor=W)
        #tree.column("col1", width=80, minwidth=80, anchor=W)
        #tree.column("col2", width=80, minwidth=80, anchor=W)
        self.tree.heading("id", text="ID")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("autor", text="Autor")
        self.tree.heading("editorial", text="Editorial")
        self.tree.heading("anio", text="Año")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("comentario", text="Comentario")
        self.tree.grid(column=0, row=5, columnspan=6)

        ##### ESTE ES EL TREEVIEW


        ###### LLENAR EL TREEVIEW
        
        base.cargar_libros(self.tree)

        ###### LLENAR EL TREEVIEW



        self.root.mainloop()


# ventana para agregar una nueva categoria
    @staticmethod
    def nueva_categoria():
        base = Base()    
        def guardar_categoriain():
            categoria = entry_categoria.get()

            #Valida los caracteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(categoria)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados

            resultado = base.buscar_categoria(categoria)

            if resultado:            
                label_aviso.config(text="Categoría Existente", fg="red")
                showerror("Error", "Categoría Existente") 
                top.after(0, lambda: top.focus_force())           
            else:            
                base.guardar_categoria(categoria)
                label_aviso.config(text=f"Categoría '{categoria}' Guardada", fg="green")
                showinfo("Guardado", "Categoría guardada") 
                top.after(0, lambda: top.focus_force())           
                entry_categoria.delete(0, 'end') 

        top = Toplevel()
        top.title("Nueva Categoría")
        top.geometry("300x150")
        

        label_categoria = Label(top, text="Ingrese nueva Categoría:")
        label_categoria.pack()

        entry_categoria = Entry(top)
        entry_categoria.pack()

        btn_guardar = Button(top, text="Guardar", command=guardar_categoriain)
        btn_guardar.pack()
        label_aviso = Label(top)  
        label_aviso.pack()  

    #Ventana para modificar categorias
    #@staticmethod
    def modificar_categoria(self,):
        base = Base()
        root = self.root
        #global root, tree
        nombre = None
        def guardar_modcategoriain(nombre):
            categoriamod = entry_nombre.get()  

            #Valida los caracteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(categoriamod)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados



            resultado = base.guardar_mod_categoria(nombre, categoriamod)
            if resultado:            
                label_aviso.config(text="Modificación exitosa", fg="Green")
                showinfo("Modificar", "Categoría modificada") 
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al modificar la categoría", fg="red")            
                showerror("Error", "Error al modificar la categoría")
                top.after(0, lambda: top.focus_force())
                

        #funcion para pasar texto al combobox
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            #nombre = valor_seleccionado.split(' ')[1]
            partes = valor_seleccionado.split(' ', 1)
            if len(partes) > 1:
                nombre = partes[1]
                entry_nombre.delete(0, 'end')
                entry_nombre.insert(0, nombre)
                

        top = Toplevel()
        top.title("Modificar Categoría")
        top.geometry("300x150")

        ####Combobox 
        categorias = base.buscar_categorias()        
        combo = ttk.Combobox(top, values=categorias)
        combo.pack()
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox
    
        entry_nombre = ttk.Entry(top)
        entry_nombre.pack(pady=10)
        
        btn_guardar = Button(top, text="Guardar modificación", command=lambda: guardar_modcategoriain(nombre))
        btn_guardar.pack()
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes
    
    #@staticmethod
    def eliminar_categoria(self,):
        #global root, tree
        base = Base()
        nombre = None
        root = self.root

        def eliminar_categoriain(nombre):
            #categoriamod = entry_nombre.get()        
            resultado = base.borrar_categoria(nombre)
            if resultado:            
                label_aviso.config(text="Borrado exitosa", fg="Green")  
                showinfo("Borrado", "Borrado Exitoso")
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al borrar la categoría", fg="red") 
                showerror("Error", "Error al borrar la categoría")
                top.after(0, lambda: top.focus_force())            
                

        #funcion para pasar la variable del combobox
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            #nombre = valor_seleccionado.split(' ')[1]     
            partes = valor_seleccionado.split(' ', 1)
            if len(partes) > 1:
                nombre = partes[1]

        top = Toplevel()
        top.title("Borrar Categoría")
        top.geometry("300x150")
        
        ####Combobox 
        categorias = base.buscar_categorias()        
        combo = ttk.Combobox(top, values=categorias)
        combo.pack(pady=10)
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox   
        
        btn_borrar = Button(top, text="Borrar", command=lambda: eliminar_categoriain(nombre))
        btn_borrar.pack(pady=10)
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes

    # ventana para agregar una nueva editorial
    @staticmethod
    def nueva_editorial():  
        #global root, tree  
        base = Base()
        def guardar_editorialin():
            editorial = entry_editorial.get()
            
            #Valida los caracteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(editorial)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados


            resultado = base.buscar_editorial(editorial)
            if resultado:            
                label_aviso.config(text="Editorial Existente", fg="red")
                showerror("Error", "Editorial Existente") 
                top.after(0, lambda: top.focus_force())           
            else:            
                base.guardar_editorial(editorial)
                label_aviso.config(text=f"Editorial '{editorial}' Guardada", fg="green")
                showinfo("Guardado", "Editorial guardada") 
                top.after(0, lambda: top.focus_force())           
                entry_editorial.delete(0, 'end') 

        top = Toplevel()
        top.title("Nueva Editorial")
        top.geometry("300x150")
        

        label_editorial = Label(top, text="Ingrese nueva Editorial:")
        label_editorial.pack()

        entry_editorial = Entry(top)
        entry_editorial.pack()

        btn_guardar = Button(top, text="Guardar", command=guardar_editorialin)
        btn_guardar.pack()
        label_aviso = Label(top)  
        label_aviso.pack()  

    #Ventana para modificar editorial
    #@staticmethod
    def modificar_editorial(self,):
        #global root, tree
        base = Base()
        nombre = None
        root = self.root
        def guardar_modeditorialin(nombre):
            editorialmod = entry_nombre.get()
            #Valida los carácteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(editorialmod)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return        
            #Valida los carácteres ingresados
            resultado = base.guardar_mod_editorial(nombre, editorialmod)
            if resultado:            
                label_aviso.config(text="Modificación exitosa", fg="Green")
                showinfo("Modificar", "Editorial modificada") 
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al modificar la Editorial", fg="red")            
                showerror("Error", "Error al modificar la Editorial")
                top.after(0, lambda: top.focus_force())
                

        #funcion para pasar texto al combobox
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            #nombre = valor_seleccionado.split(' ')[1]
            partes = valor_seleccionado.split(' ', 1)
            if len(partes) > 1:
                nombre = partes[1]
                entry_nombre.delete(0, 'end')
                entry_nombre.insert(0, nombre)   

        top = Toplevel()
        top.title("Modificar Categoría")
        top.geometry("300x150")
        
        ####Combobox 
        editoriales = base.buscar_editoriales()        
        combo = ttk.Combobox(top, values=editoriales)
        combo.pack()
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox
    
        entry_nombre = ttk.Entry(top)
        entry_nombre.pack(pady=10)
        
        btn_guardar = Button(top, text="Guardar modificación", command=lambda: guardar_modeditorialin(nombre))
        btn_guardar.pack()
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes

    #@staticmethod
    def eliminar_editorial(self,):
        #global root, tree
        base = Base()
        root = self.root
        nombre = None
        def eliminar_editorialin(nombre):
            #categoriamod = entry_nombre.get()        
            resultado = base.borrar_editorial(nombre)
            if resultado:            
                label_aviso.config(text="Borrado exitosa", fg="Green")  
                showinfo("Borrado", "Borrado Exitoso")
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al borrar la editorial", fg="red") 
                showerror("Error", "Error al borrar la editorial")
                top.after(0, lambda: top.focus_force())            
                

        #funcion para pasar la variable del combobox
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            #nombre = valor_seleccionado.split(' ')[1]       
            partes = valor_seleccionado.split(' ', 1)   
            if len(partes) > 1:
                nombre = partes[1]

        top = Toplevel()
        top.title("Borrar Editorial")
        top.geometry("300x150")
        
        ####Combobox 
        editoriales = base.buscar_editoriales()        
        combo = ttk.Combobox(top, values=editoriales)
        combo.pack(pady=10)
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox   
        
        btn_borrar = Button(top, text="Borrar", command=lambda: eliminar_editorialin(nombre))
        btn_borrar.pack(pady=10)
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes

    # ventana para agregar un nuevo autor
    @staticmethod
    def nuevo_autor():    
        #global root, tree
        base = Base()
        def guardar_autorin():
            autor = entry_autor.get()

            #Valida los caracteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(autor)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados

            resultado = base.buscar_autor(autor)
            if resultado:            
                label_aviso.config(text="Autor Existente", fg="red")
                showerror("Error", "Autor Existente") 
                top.after(0, lambda: top.focus_force())           
            else:            
                base.guardar_autor(autor)
                label_aviso.config(text=f"Autor '{autor}' Guardada", fg="green")
                showinfo("Guardado", "Autor guardado") 
                top.after(0, lambda: top.focus_force())           
                entry_autor.delete(0, 'end') 

        top = Toplevel()
        top.title("Nuevo autor")
        top.geometry("300x150")
        

        label_autor = Label(top, text="Ingrese nuevo Autor:")
        label_autor.pack()

        entry_autor = Entry(top)
        entry_autor.pack()

        btn_guardar = Button(top, text="Guardar", command=guardar_autorin)
        btn_guardar.pack()
        label_aviso = Label(top)  
        label_aviso.pack()  


    #Ventana para modificar autores
    #@staticmethod
    def modificar_autor(self,):
        #global root, tree
        base = Base()
        nombre = None
        root = self.root
        def guardar_modautorin(nombre):
            autormod = entry_nombre.get()  

            #Valida los caracteres ingresados
            patron = re.compile("^[a-zA-Z0-9 ]+$")
            match = patron.search(autormod)

            if not match:
                showerror("Error", "Algunos carácteres introducidos no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados

            resultado = base.guardar_mod_autor(nombre, autormod)
            if resultado:            
                label_aviso.config(text="Modificación exitosa", fg="Green")
                showinfo("Modificar", "Autor modificado") 
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al modificar autor", fg="red")            
                showerror("Error", "Error al modificar autor")
                top.after(0, lambda: top.focus_force())
                

        #funcion para pasar texto al combobox
        #def seleccionar_item(event):
        #    nonlocal nombre
        #    valor_seleccionado = combo.get()
        #    nombre = valor_seleccionado.split(' ')[1]
        #    entry_nombre.delete(0, 'end')
        #    entry_nombre.insert(0, nombre)    
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            partes = valor_seleccionado.split(' ', 1)
            if len(partes) > 1:
                nombre = partes[1]
                entry_nombre.delete(0, 'end')
                entry_nombre.insert(0, nombre)
                
        top = Toplevel()
        top.title("Modificar Autor")
        top.geometry("300x150")
        
        ####Combobox 
        autores = base.buscar_autores()        
        combo = ttk.Combobox(top, values=autores)
        combo.pack()
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox
    
        entry_nombre = ttk.Entry(top)
        entry_nombre.pack(pady=10)
        
        btn_guardar = Button(top, text="Guardar modificación", command=lambda: guardar_modautorin(nombre))
        btn_guardar.pack()
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes

    #@staticmethod
    def eliminar_autor(self,):
        nombre = None
        base = Base()
        root = self.root
        def eliminar_autorin(nombre):
            #categoriamod = entry_nombre.get()        
            resultado = base.borrar_autor(nombre)
            if resultado:            
                label_aviso.config(text="Borrado exitosa", fg="Green")  
                showinfo("Borrado", "Borrado Exitoso")
                top.after(1000, lambda: top.destroy())
                top.after(1000, lambda: root.focus_force())     
            else:            
                label_aviso.config(text=f"Error al borrar autor", fg="red") 
                showerror("Error", "Error al borrar autor")
                top.after(0, lambda: top.focus_force())            
                

        #funcion para pasar la variable del combobox
        def seleccionar_item(event):
            nonlocal nombre
            valor_seleccionado = combo.get()
            #nombre = valor_seleccionado.split(' ')[1]    
            partes = valor_seleccionado.split(' ', 1)
            if len(partes) > 1:
                nombre = partes[1]

        top = Toplevel()
        top.title("Borrar Autor")
        top.geometry("300x150")
        
        ####Combobox 
        autores = base.buscar_autores()        
        combo = ttk.Combobox(top, values=autores)
        combo.pack(pady=10)
        combo.bind("<<ComboboxSelected>>", seleccionar_item)
        ####Combobox   
        
        btn_borrar = Button(top, text="Borrar", command=lambda: eliminar_autorin(nombre))
        btn_borrar.pack(pady=10)
        
        #### Label de notificación de mensajes
        label_aviso = Label(top)  
        label_aviso.pack()  
        #### Label de notificación de mensajes

    # ventana para agregar una nuevo libro
    #@staticmethod
    def nuevo_libro(self):
        #global root, tree
        base = Base()
        #root = Ventana.root
        tree = self.tree
        def guardar_libroin():
            libro = entry_libro.get()
            autor = combo_autores.get()
            editorial = combo_editoriales.get()
            genero = combo_categorias.get()
            anio = entry_anio.get()
            comentario = text_comentario.get("1.0", "end-1c")



            #Valida los caracteres ingresados en el titulo
            patron = re.compile("^[a-zA-Z0-9ÁÉÍÓÚáéíóúÜü ]+$")
            match = patron.search(libro)

            if not match:
                showerror("Error", "Algunos carácteres introducidos en el libro no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados en el titulo
            #Valida los caracteres ingresados en el año

            patron = re.compile("^(1\d{3}|2\d{3})$")  # Expresión regular para años entre 1000 y 2999
            match = patron.match(anio)

            if not match:
                showerror("Error", "El año es incorrecto") 
                top.after(0, lambda: top.focus_force()) 
                return
            
            #Valida los caracteres ingresados en el año
            #Valida los caracteres ingresados en los comentarios
            patron = re.compile("^[a-zA-Z0-9ÁÉÍÓÚáéíóúÜü ]*$")
            match = patron.search(comentario)

            if not match:
                showerror("Error", "Algunos carácteres introducidos en los comentarios no son válidos") 
                top.after(0, lambda: top.focus_force()) 
                return
            #Valida los caracteres ingresados en los comentarios


            resultado = base.buscar_libro(libro)
            if resultado:            
                label_aviso.config(text="Libro Existente", fg="red")
                showerror("Error", "Libro Existente") 
                top.after(0, lambda: top.focus_force())           
            else:            
                base.guardar_libro(libro, autor, editorial, anio, genero, comentario)
                label_aviso.config(text=f"Libro '{libro}' Guardado", fg="green")
                showinfo("Guardado", "Libro guardado") 
                top.after(0, lambda: top.focus_force())           
                entry_libro.delete(0, 'end') 
                #Ventana.limpiar_treeview(tree)
                self.limpiar_treeview()
                #Ventana.cargar_libros(tree)
                base.cargar_libros(tree)

        # Verifica la longitud del campo de comentarios
        def limitar_longitud(event):
            comentario = text_comentario.get("1.0", "end-1c")
            if len(comentario) > 255:
                text_comentario.delete("end-1c", "end")  

        top = Toplevel()
        top.title("Nuevo Libro")
        top.geometry("300x400")
        

        label_libro = Label(top, text="Ingrese nuevo Libro:")
        label_libro.pack()

        entry_libro = Entry(top)
        entry_libro.pack()

        ####Combobox autor
        label_autor = Label(top, text="Autor:")
        label_autor.pack()
        autores = base.buscar_autores()        
        combo_autores = ttk.Combobox(top, values=autores)
        combo_autores.pack()
        ####Combobox autor
        ####Combobox genero
        label_genero = Label(top, text="Genero:")
        label_genero.pack()
        categorias = base.buscar_categorias()        
        combo_categorias = ttk.Combobox(top, values=categorias)
        combo_categorias.pack()
        ####Combobox genero
        ####Combobox genero
        label_editorial = Label(top, text="Editorial:")
        label_editorial.pack()
        editoriales = base.buscar_editoriales()        
        combo_editoriales = ttk.Combobox(top, values=editoriales)
        combo_editoriales.pack()
        ####Combobox genero
        ####Entry año
        label_anio = Label(top, text="Año:")
        label_anio.pack()
        
        entry_anio = Entry(top)
        entry_anio.pack()
        ####Entry año
        #### Text comentario ####
        label_comentario = Label(top, text="Comentarios:")
        label_comentario.pack()
        text_comentario = Text(top, height=9, width=30)  
        text_comentario.pack()
        text_comentario.bind("<Key>", limitar_longitud)
        #### Text comentario ####



        btn_guardar = Button(top, text="Guardar", command=guardar_libroin)
        btn_guardar.pack()
        label_aviso = Label(top)  
        label_aviso.pack()  

    #@staticmethod
    def eliminar_libro(self):    
        #global root, tree
        tree = self.tree
        base = Base()
        def eliminar_libro_seleccionado():
            seleccion = tree.focus()
            datos = tree.item(seleccion)
            libro_id = datos['values'][0] 

            
            resultado = base.eliminar_libro_db(libro_id)
            if resultado:        
                tree.delete(seleccion)
                showinfo("Borrado", "Libro Borrado")             
            else:
                showerror("Error", "Error al borrar") 

        top = Toplevel()
        top.title("Eliminar Libro")
        label_info = Label(top, text="Seleccione un libro en el treeview y presione el botón para borrar")
        label_info.pack()
        

        top.geometry("300x150")

        btn_eliminar = Button(top, text="Eliminar Libro", command=eliminar_libro_seleccionado)
        btn_eliminar.pack()
