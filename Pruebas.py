from PIL import Image
from tkinter import messagebox
import datetime
import os

downloadsFolder = os.path.join(os.environ["USERPROFILE"], "Downloads/")
picturesFolder = os.path.join(os.environ["USERPROFILE"], "Downloads/Imagenes/")
iconsFolder = os.path.join(os.environ["USERPROFILE"], "Downloads/Imagenes/ICONOS/ICO/")
documentsFolder = os.path.join(os.environ["USERPROFILE"], "Downloads/Documentos/")
swfolder = os.path.join(os.environ["USERPROFILE"], "Downloads/PROGRAMAS/")
otherfolder = os.path.join(os.environ["USERPROFILE"], "Downloads/Varios/")
incidencias = "C:/Users/soporte_ext/OneDrive - Network Steel Resources, S.A/Documentos/REVISIONES/SEMANAL/INCIDENCIAS (Viernes)/HISTORICO/"
Comparativa = "C:/Users/soporte_ext/OneDrive - Network Steel Resources, S.A/Documentos/REVISIONES/SEMANAL/COMPARATIVA DE EQUIPOS (Miercoles)/"
compressedfolder = os.path.join(os.environ["USERPROFILE"], "Downloads/Comprimidos/")
fecha = str(datetime.datetime.now().strftime("%y%m%d"))

if __name__ == "__main__":

    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)
