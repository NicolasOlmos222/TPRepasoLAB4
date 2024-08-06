from Clase import *
import tkinter as tk
from tkinter import messagebox

listaLibros = []

'''
def menu():
    print("1. Listar")
    print("2. Agregar")
    print("3. Modificar")
    print("4. Eliminar")
    print("5. Salir")
    return int(input("Elige una opción: "))

while True:
    op = menu()
    if op == 1:
        for i in listaLibros:
            i.mostrar()
    elif op == 2:
        listaLibros.append(Libro(input("Titulo: "), input("Autor: "), input("Editorial: "), input("Genero: "), input("Ubicacion: "), int(input("Cantidad: "))))
    elif op == 3:
        libro = input("Ingrese el nombre del libro a modificar: ")
        for i in listaLibros:
            if i.titulo == libro:
                i.modificar(input("Titulo: "), input("Autor: "), input("Editorial: "), input("Genero: "), input("Ubicacion: "), int(input("Cantidad: ")))
    elif op == 4:
        libro = input("Ingrese el nombre del libro a eliminar: ")
        for i in listaLibros:
            if i.titulo == libro:
                listaLibros.remove(i)
    elif op == 5:
        print("salir")
        break
    else:
        print("Opción incorrecta")

'''

def guardar():
    global listaLibros, Libro, textoNombre, textoAutor, textoEditorial, textoGenero, textoUbicacion, textoCantidad
    listaLibros.append(Libro(textoNombre.get(), textoAutor.get(), textoEditorial.get(), textoGenero.get(), textoUbicacion.get(), textoCantidad.get()))
    messagebox.showinfo("Guardar", "Libro guardado!")

def eliminar():
    global listaLibros, textoNombre
    bandera = False
    for i in listaLibros:
        if i.titulo == textoNombre.get():
            listaLibros.remove(i)
            bandera = True
    if bandera:
        messagebox.showinfo("Eliminar", "Libro eliminado!")
    else:
        messagebox.showinfo("Eliminar", "Libro no encontrado!")

def modificar():
    global listaLibros, textoNombre, textoAutor, textoEditorial, textoGenero, textoUbicacion, textoCantidad
    bandera = False
    for i in listaLibros:
        if i.titulo == textoNombre.get():
            i.modificar(textoNombre.get(), textoAutor.get(), textoEditorial.get(), textoGenero.get(), textoUbicacion.get(), textoCantidad.get())
            bandera = True
    if bandera:
        messagebox.showinfo("Modificar", "Libro modificado!")
    else:
        messagebox.showinfo("Modificar", "Libro no encontrado!")

def listar():
    global listaLibros
    cant = 1
    listbox.delete(0, tk.END) 
    for libro in listaLibros:
        listbox.insert(tk.END, f"Libro N°{cant}")
        listbox.insert(tk.END, f"Nombre: {libro.getTitulo()}")
        listbox.insert(tk.END, f"Autor: {libro.getAutor()}")
        listbox.insert(tk.END, f"Editorial: {libro.getEditorial()}")
        listbox.insert(tk.END, f"Género: {libro.getGenero()}")
        listbox.insert(tk.END, f"Ubicación: {libro.getUbicacion()}")
        listbox.insert(tk.END, f"Cantidad: {libro.getCantidad()}")
        listbox.insert(tk.END, "")
        cant += 1


root = tk.Tk()
root.title("Interfaz en Tkinter")
root.geometry("600x400")

frame_columna1 = tk.Frame(root)
frame_columna1.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame_columna1, text="Nombre").grid(row=0, column=0, sticky="w")
textoNombre = tk.Entry(frame_columna1)
textoNombre.grid(row=0, column=1, pady=5)

tk.Label(frame_columna1, text="Autor").grid(row=1, column=0, sticky="w")
textoAutor = tk.Entry(frame_columna1)
textoAutor.grid(row=1, column=1, pady=5)

tk.Label(frame_columna1, text="Editorial").grid(row=2, column=0, sticky="w")
textoEditorial = tk.Entry(frame_columna1)
textoEditorial.grid(row=2, column=1, pady=5)

tk.Label(frame_columna1, text="Género").grid(row=3, column=0, sticky="w")
textoGenero = tk.Entry(frame_columna1)
textoGenero.grid(row=3, column=1, pady=5)

tk.Label(frame_columna1, text="Ubicación").grid(row=4, column=0, sticky="w")
textoUbicacion = tk.Entry(frame_columna1)
textoUbicacion.grid(row=4, column=1, pady=5)

tk.Label(frame_columna1, text="Cantidad").grid(row=5, column=0, sticky="w")
textoCantidad = tk.Entry(frame_columna1)
textoCantidad.grid(row=5, column=1, pady=5)

guardar_button = tk.Button(frame_columna1, text="Guardar", command=guardar, width=16)
guardar_button.grid(row=6, column=0, pady=5)

eliminar_button = tk.Button(frame_columna1, text="Eliminar por nombre", command=eliminar, width=16)
eliminar_button.grid(row=7, column=0, pady=5)

modificar_button = tk.Button(frame_columna1, text="Modificar por nombre", command=modificar, width=16)
modificar_button.grid(row=8, column=0, pady=5)

listar_button = tk.Button(frame_columna1, text="Listar", command=listar, width=16)
listar_button.grid(row=9, column=0, pady=5)

frame_columna2 = tk.Frame(root)
frame_columna2.grid(row=0, column=1, padx=10, pady=10)

listbox = tk.Listbox(frame_columna2, width=25, height=20)
scrollbar = tk.Scrollbar(frame_columna2, orient="vertical", command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
