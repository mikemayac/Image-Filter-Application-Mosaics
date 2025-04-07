import streamlit as st
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
import time
import math

# Configuración de la página
st.set_page_config(page_title="Filtro AT&T", layout="wide")


def convertir_a_grises(imagen):
    """Convierte una imagen a escala de grises."""
    return ImageOps.grayscale(imagen)


def aplicar_alto_contraste(imagen, umbral=128):
    """Convierte la imagen a blanco y negro puro."""
    imagen_array = np.array(imagen)
    imagen_bn = np.where(imagen_array > umbral, 255, 0).astype(np.uint8)
    return Image.fromarray(imagen_bn)


def aplicar_filtro_att(imagen_bn, grosor_linea=5):
    """
    Aplica el filtro de estilo AT&T basado en las imágenes de ejemplo.
    """
    # Convertir a array para manipulación
    img_array = np.array(imagen_bn)
    altura, ancho = img_array.shape

    # Crear una imagen de salida en blanco (toda blanca)
    resultado = np.ones((altura, ancho), dtype=np.uint8) * 255

    # Centro vertical y horizontal de la imagen
    centro_y = altura // 2
    centro_x = ancho // 2

    # Radio máximo del "globo" (algo menor que el ancho/altura para asegurar forma circular)
    radio_max = min(ancho, altura) // 2 * 0.95

    # Para cada franja horizontal
    for y in range(0, altura, grosor_linea * 2):
        # Determinar la altura de esta franja
        inicio_franja = y
        fin_franja = min(y + grosor_linea, altura)

        # Calcular distancia vertical desde el centro
        distancia_vertical = abs(y + grosor_linea // 2 - centro_y)

        # Calcular qué ancho debe tener esta franja según la fórmula del círculo
        if distancia_vertical < radio_max:
            # Fórmula del círculo: x² + y² = r²
            medio_ancho = int(math.sqrt(radio_max ** 2 - distancia_vertical ** 2))
        else:
            # Fuera del círculo
            continue

        # Calcular inicio y fin en el eje x para esta franja
        inicio_x = max(0, centro_x - medio_ancho)
        fin_x = min(ancho, centro_x + medio_ancho)

        # Extraer la información de esta franja desde la imagen original
        for x in range(inicio_x, fin_x):
            # Copiamos píxeles de la imagen original a la franja
            resultado[inicio_franja:fin_franja, x] = img_array[inicio_franja:fin_franja, x]

    return Image.fromarray(resultado)


def main():
    st.sidebar.title("Configuraciones")

    # Configuraciones del filtro
    st.sidebar.markdown("### Filtro AT&T")
    grosor_linea = st.sidebar.slider("Grosor de línea", 1, 20, 5)
    contraste = st.sidebar.slider("Umbral de contraste", 50, 200, 128)

    # Uploader para cargar la imagen
    uploaded_file = st.sidebar.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])
    imagen_resultante = None
    buf_value = None

    if uploaded_file is not None:
        # Cargamos la imagen original
        imagen_original = Image.open(uploaded_file).convert("RGB")

        # Aplicar el filtro AT&T
        with st.spinner("Aplicando el filtro AT&T..."):
            inicio = time.time()

            # Paso 1: Convertir a escala de grises
            imagen_gris = convertir_a_grises(imagen_original)

            # Paso 2: Aplicar alto contraste (blanco y negro)
            imagen_bn = aplicar_alto_contraste(imagen_gris, contraste)

            # Paso 3: Aplicar el filtro AT&T
            imagen_resultante = aplicar_filtro_att(imagen_bn, grosor_linea)

            tiempo_procesamiento = time.time() - inicio
            st.sidebar.info(f"Tiempo: {tiempo_procesamiento:.2f} segundos")

        # Preparar para descarga
        buf = BytesIO()
        imagen_resultante.save(buf, format="PNG")
        buf_value = buf.getvalue()

    # Título y botón de descarga
    title_col, button_col = st.columns([4, 1])
    with title_col:
        st.title("Filtro Estilo AT&T")
    with button_col:
        if imagen_resultante is not None and buf_value is not None:
            st.download_button(
                label="⬇️ Descargar",
                data=buf_value,
                file_name="imagen_att.png",
                mime="image/png",
                key="download_button"
            )

    # Mostrar imágenes
    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.image(imagen_original, caption="Imagen Original", use_container_width=True)
        with col2:
            st.image(imagen_resultante, caption="Imagen con Filtro AT&T", use_container_width=True)
    else:
        st.info("Sube una imagen para aplicar el filtro AT&T.")
        st.markdown("""
        ## Efecto AT&T
        Este filtro recrea el efecto usado en los Laboratorios Bell en 1985, 
        que transforma fotografías en un estilo similar al logotipo de AT&T.

        Ajusta el grosor de línea y el contraste para obtener diferentes resultados.
        """)


if __name__ == "__main__":
    main()