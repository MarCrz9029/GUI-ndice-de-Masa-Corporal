import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import csv

# Función para calcular el Índice de Masa Corporal (IMC)
def calcularImc():
    # Obtener los valores de peso, altura, edad y sexo de las entradas
    peso = float(entryPeso.get())
    altura = float(entryAltura.get())
    edad = int(entryEdad.get())
    sexo = varSexo.get()

    # Validar que la altura no sea 0 para evitar división por cero
    if altura == 0:
        messagebox.showerror("Error", "La altura no puede ser 0")
        return

    # Definir el factor ks según el sexo
    if sexo == "Hombre":
        ks = 1.0
    else:
        ks = 1.1

    # Calcular el factor ka basado en la edad
    ka = 1 + 0.01 * (edad - 25)
    
    # Calcular el IMC usando los factores ks y ka
    imc = peso / (altura**2) * ks * ka

    # Determinar la categoría del IMC
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    # Actualizar la etiqueta de resultado con el IMC y la categoría
    labelResultado.config(text=f"IMC: {imc:.2f} - {categoria}")
    return imc, categoria

# Función para guardar los datos en un archivo CSV
def guardarDatos():
    # Obtener los valores de las entradas
    nombre = entryNombre.get()
    peso = entryPeso.get()
    altura = entryAltura.get()
    edad = entryEdad.get()
    sexo = varSexo.get()
    
    # Calcular el IMC y la categoría
    imc, categoria = calcularImc()

    # Preparar los datos para guardar
    datos = [nombre, peso, altura, edad, sexo, f"{imc:.2f}", categoria]

    # Guardar los datos en un archivo CSV con el nombre del usuario
    with open(f"{nombre}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Peso (kg)", "Altura (m)", "Edad", "Sexo", "IMC", "Categoría"])
        writer.writerow(datos)

# Función para leer datos desde un archivo CSV y mostrarlos en una nueva ventana
def leerCsv():
    # Abrir un cuadro de diálogo para seleccionar el archivo CSV
    filePath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filePath:
        # Leer los datos del archivo CSV
        with open(filePath, mode="r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Leer los encabezados
            datos = list(reader)  # Leer el resto de los datos

            # Crear una nueva ventana para mostrar los datos
            ventanaCsv = tk.Toplevel(ventanaPrincipal)
            ventanaCsv.title("Datos CSV")
            ventanaCsv.geometry("600x400")
            ventanaCsv.configure(bg='#F5F5F5')  # Fondo gris claro

            # Crear un Frame para el Treeview y el scrollbar
            frameTreeview = tk.Frame(ventanaCsv, bg='#F5F5F5')
            frameTreeview.pack(expand=True, fill="both", padx=10, pady=10)

            # Crear el Treeview con estilo
            estilo = ttk.Style()
            estilo.theme_use("clam")
            estilo.configure("Treeview",
                             background="#D3D3D3",
                             foreground="black",
                             rowheight=25,
                             fieldbackground="#D3D3D3")
            estilo.map('Treeview', background=[('selected', '#347083')])

            tree = ttk.Treeview(frameTreeview, columns=headers, show="headings", style="Treeview")
            tree.pack(expand=True, fill="both", side="left")

            # Configurar encabezados
            for header in headers:
                tree.heading(header, text=header)
                tree.column(header, width=100, anchor='center')

            # Insertar datos en el Treeview
            for row in datos:
                tree.insert("", "end", values=row)

            # Crear y agregar scrollbar
            scrollbar = ttk.Scrollbar(frameTreeview, orient="vertical", command=tree.yview)
            scrollbar.pack(side="right", fill="y")
            tree.configure(yscroll=scrollbar.set)

            # Agregar etiqueta de título
            labelTitulo = tk.Label(ventanaCsv, text="Visualización de Datos CSV", font=("Helvetica", 14, "bold"), bg='#F5F5F5')
            labelTitulo.pack(pady=10)

# Crear la ventana principal de la aplicación
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Calculadora de IMC")
ventanaPrincipal.geometry("650x500")

# Crear un canvas para poner la imagen de fondo
canvas = tk.Canvas(ventanaPrincipal, width=800, height=600)
canvas.grid(row=0, column=0, rowspan=10, columnspan=4)

# Cargar la imagen de fondo
fondoImg = ImageTk.PhotoImage(Image.open("mar.jpg"))
canvas.create_image(0, 0, anchor="nw", image=fondoImg)

# Definir fuente y color
fuente = ("Helvetica", 12, "italic")
colorFuente = "#4B0082"  # Color índigo

# Crear los widgets de entrada y etiquetas
labelNombre = tk.Label(ventanaPrincipal, text="Nombre:", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
entryNombre = tk.Entry(ventanaPrincipal, font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

labelPeso = tk.Label(ventanaPrincipal, text="Peso (kg):", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
entryPeso = tk.Entry(ventanaPrincipal, font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

labelAltura = tk.Label(ventanaPrincipal, text="Altura (m):", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
entryAltura = tk.Entry(ventanaPrincipal, font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

labelEdad = tk.Label(ventanaPrincipal, text="Edad:", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
entryEdad = tk.Entry(ventanaPrincipal, font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

labelSexo = tk.Label(ventanaPrincipal, text="Sexo:", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
varSexo = tk.StringVar(value="Hombre")
radioHombre = tk.Radiobutton(ventanaPrincipal, text="Hombre", variable=varSexo, value="Hombre", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)
radioMujer = tk.Radiobutton(ventanaPrincipal, text="Mujer", variable=varSexo, value="Mujer", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

# Cargar las imágenes para los botones
imgCalcular = ImageTk.PhotoImage(Image.open("b1.png"))
imgGuardar = ImageTk.PhotoImage(Image.open("b2.png"))
imgLeer = ImageTk.PhotoImage(Image.open("b3.png"))

# Crear botones con imágenes
botonCalcular = tk.Button(ventanaPrincipal, image=imgCalcular, command=calcularImc, borderwidth=0, cursor="hand2", highlightthickness=0, bg=None)
botonGuardar = tk.Button(ventanaPrincipal, image=imgGuardar, command=guardarDatos, borderwidth=0, cursor="hand2", highlightthickness=0, bg=None)
botonLeerCsv = tk.Button(ventanaPrincipal, image=imgLeer, command=leerCsv, borderwidth=0, cursor="hand2", highlightthickness=0, bg=None)

labelResultado = tk.Label(ventanaPrincipal, text="IMC:", font=fuente, fg=colorFuente, highlightthickness=0, bd=0, bg=None)

# Ubicar los widgets en la ventana
labelNombre.place(x=50, y=20)
entryNombre.place(x=200, y=20, width=100, height=20)

labelPeso.place(x=50, y=60)
entryPeso.place(x=200, y=60, width=100, height=20)

labelAltura.place(x=50, y=100)
entryAltura.place(x=200, y=100, width=100, height=20)

labelEdad.place(x=50, y=140)
entryEdad.place(x=200, y=140, width=100, height=20)

labelSexo.place(x=50, y=180)
radioHombre.place(x=200, y=180)
radioMujer.place(x=300, y=180)

botonCalcular.place(x=50, y=220, width=300, height=50)
labelResultado.place(x=50, y=280, width=300)

botonGuardar.place(x=50, y=320, width=300, height=50)
botonLeerCsv.place(x=50, y=380, width=300, height=50)

# Iniciar el bucle principal de la aplicación
ventanaPrincipal.mainloop()
