import cv2
import matplotlib.pyplot as plt
from ocr import OCRProcessor
import os

def mostrar_resultados(img, resultados):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen procesada")
    plt.axis("off")
    plt.show()

    print("\nResultados OCR:")
    for texto in resultados:
        print(f"Texto: {texto[1]}, Confianza: {round(texto[2]*100, 2)}%")

def main():
    carpeta = "images"
    imagenes = [f for f in os.listdir(carpeta) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not imagenes:
        print(f"No se encontraron imágenes en la carpeta '{carpeta}'.")
        return

    ocr = OCRProcessor()

    for img_file in imagenes:
        ruta_img = os.path.join(carpeta, img_file)
        img, resultados = ocr.procesar_imagen(ruta_img)
        if img is not None:
            mostrar_resultados(img, resultados)

if __name__ == "__main__":
    main()
