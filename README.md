# Aplicación de Filtro AT&T

### Recreación del efecto visual de los Laboratorios Bell

Esta aplicación web creada con **Python** y **Streamlit** permite aplicar el histórico **filtro AT&T** a imágenes digitales, recreando el emblemático efecto visual desarrollado en los Laboratorios Bell en 1985.

El filtro transforma fotografías normales en un estilo que recuerda al logotipo de AT&T, caracterizado por franjas horizontales que forman un patrón globular. El proceso consta de tres pasos principales:
1. **Conversión a escala de grises** de la imagen original
2. **Aplicación de alto contraste** para obtener una imagen en blanco y negro puro
3. **Generación del patrón de franjas horizontales** siguiendo la forma circular del logo de AT&T

Este efecto, originalmente creado por Tom Duff, ganó notoriedad cuando fue utilizado con la fotografía de Peter Weinberger, uno de los jefes de departamento de los Laboratorios Bell.

---

## Requisitos

- Python 3.8 o superior
- [Streamlit](https://docs.streamlit.io/) para la creación de la interfaz web
- [Pillow](https://pillow.readthedocs.io/) (PIL) para la manipulación de imágenes
- NumPy para el procesamiento de arrays de imagen
- Math para los cálculos del patrón circular

En el archivo **requirements.txt** se listan las dependencias necesarias. Asegúrate de instalarlas antes de ejecutar la aplicación.

---

## Instalación

1. **Clona** este repositorio en tu máquina local.
2. Crea y activa un **entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # En Windows: venv\Scripts\activate
   ```
3. Instala los paquetes necesarios:
   ```bash
   pip install -r requirements.txt
   ```

---

## Ejecución de la Aplicación

1. Dentro del entorno virtual, ubícate en la carpeta donde se encuentra el archivo principal.
2. Ejecuta:
   ```bash
   streamlit run att.py
   ```
3. Automáticamente se abrirá tu navegador mostrando la interfaz de la aplicación.  
   Si no se abre, copia la URL que aparece en la terminal y pégala en tu navegador.

---

## Uso de la Aplicación

1. **Sube una imagen** en la barra lateral (sidebar), en formatos `JPG`, `JPEG` o `PNG`.
2. Ajusta los parámetros del filtro:
   - **Grosor de línea**: Define el ancho de las franjas horizontales (valores recomendados entre 3 y 10)
   - **Umbral de contraste**: Ajusta la sensibilidad del filtro de alto contraste (valores entre 50 y 200)
3. **Observa** cómo se muestra la **imagen original** en una columna y la **imagen con el filtro AT&T** en la otra.
4. **Descarga** la imagen procesada haciendo clic en el botón de descarga que aparece sobre la imagen resultante.

---

## Algoritmo Implementado

El algoritmo implementado:

1. **Convierte la imagen a escala de grises** utilizando las funciones optimizadas de PIL
2. **Aplica un filtro de alto contraste** para convertir la imagen a blanco y negro puro
3. **Genera el patrón de franjas horizontales** siguiendo un patrón circular:
   - Calcula el centro y radio máximo de un círculo virtual
   - Para cada franja horizontal, determina su ancho según la ecuación del círculo (x² + y² = r²)
   - Copia los píxeles de la imagen original en blanco y negro a las franjas correspondientes

---

## Estructura del Proyecto

```bash
.
├── att.py                # Código principal de la aplicación 
├── .streamlit/           # Carpeta de configuración de Streamlit 
│    └── config.toml      # Configuraciones extra de Streamlit
├── README.md             # Archivo de documentación
├── requirements.txt      # Dependencias del proyecto
└── venv/                 # Entorno virtual 
```

## Referencias

- Holzmann, G. (1988). Beyond Photography - The Digital Darkroom.
- Documentación y artículos históricos sobre los Laboratorios Bell y el desarrollo del logotipo de AT&T.