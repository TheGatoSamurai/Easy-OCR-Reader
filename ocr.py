import easyocr
import cv2

class OCRProcessor:
    def __init__(self, language='es'):
        self.reader = easyocr.Reader([language])
    
    def procesar_imagen(self, img_path):
        print(f"\nProcesando imagen: {img_path}")
        img = cv2.imread(img_path)
        if img is None:
            print("Error: No se pudo cargar la imagen.")
            return None, []

        img = cv2.resize(img, (600, 400))
        resultado = self.reader.readtext(img)
        return img, resultado
