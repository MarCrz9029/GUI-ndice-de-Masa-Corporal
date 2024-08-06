# Calculadora de IMC con Interfaz Gráfica

Este proyecto es una calculadora de Índice de Masa Corporal (IMC) desarrollada en Python utilizando la biblioteca Tkinter para la interfaz gráfica de usuario. La aplicación permite calcular el IMC basado en los datos ingresados por el usuario y clasificarlo en diferentes categorías. Además, los datos pueden guardarse en un archivo CSV y leerse para visualizarse posteriormente.

## Funcionalidades

1. **Calcular IMC**: Calcula el IMC basado en el peso, altura, edad y sexo del usuario, y lo clasifica en una categoría.
2. **Guardar Datos**: Guarda los datos ingresados por el usuario en un archivo CSV con el nombre del usuario.
3. **Leer y Visualizar Datos CSV**: Lee los datos desde un archivo CSV seleccionado por el usuario y los muestra en una nueva ventana con un `Treeview` estilizado.

## Archivos Incluidos

- `main.py`: El archivo principal que contiene el código de la aplicación.
- `mar.jpg`: Imagen de fondo utilizada en la interfaz gráfica.
- `b1.png`, `b2.png`, `b3.png`: Imágenes para los botones de calcular, guardar y leer CSV.


### Uso de la Aplicación

1. **Calcular IMC**:
- Ingrese su nombre, peso, altura, edad y seleccione su sexo.
- Haga clic en el botón de "Calcular" (representado por la imagen `b1.png`).
- El resultado del IMC y su categoría se mostrarán en la interfaz.

2. **Guardar Datos**:
- Después de calcular su IMC, haga clic en el botón de "Guardar" (representado por la imagen `b2.png`).
- Los datos se guardarán en un archivo CSV con el nombre ingresado.

3. **Leer y Visualizar Datos CSV**:
- Haga clic en el botón de "Leer CSV" (representado por la imagen `b3.png`).
- Seleccione el archivo CSV deseado.
- Una nueva ventana se abrirá mostrando los datos del archivo CSV en una tabla.

### Personalización

- **Cambiar imagen de fondo**:
- Reemplace `mar.jpg` con cualquier otra imagen de su elección.
- Asegúrese de actualizar el nombre del archivo en el código si es necesario.

- **Actualizar Estilo**:
- Los estilos de los widgets pueden personalizarse modificando las propiedades en el código, como `font`, `fg`, `bg`, etc.

## Autor

Desarrollado por Mar Crz Mrz.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.


### Requisitos

- Python 3.6
- Bibliotecas: tkinter, PIL (Pillow)

### Repositorio
- https://github.com/MarCrz9029/GUI-ndice-de-Masa-Corporal.git

