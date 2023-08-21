import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from tkinter.filedialog import askdirectory
import shutil

# Preguntar por la ruta de la carpeta
Carpeta = askdirectory(title='Seleccionar carpeta')
os.chdir(Carpeta) 

# Obtener todos los archivos PDF de la carpeta Folder y sus subcarpetas
pdfFiles = []
for foldername, subfolders, filenames in os.walk(Carpeta):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFiles.append(os.path.join(foldername, filename))

#pdfFiles.sort(key=str.lower) # Ordenar los archivos alfabéticamente 

#Ordenar los archivos alfabéticamente sin tener en cuenta el path
pdfFiles.sort(key=os.path.basename)

#ordenar pdf_files por nombre
#pdf_files.sort()

temp = Carpeta + "/Temp"

# Crear carpeta Temp
if not os.path.exists(temp):
    os.makedirs(temp)

#Copiar los archivos de pdf_files a la carpeta Temp
for pdf in pdfFiles:
    shutil.copy(pdf, temp)

#Listar todos los archivos de la carpeta Temp en pdf_files con el path completo
pdf_files = [temp + "/" + f for f in os.listdir(temp) if f.endswith(".pdf")]

# create pdf merger object
merger = PdfMerger()

# agregar las ultimas páginas de cada archivo pdf al merger 
for pdf in pdf_files:

    with open(pdf, 'rb') as f:

        pdf_reader = PdfReader(f)

        number_of_pages = len(pdf_reader.pages) -1

        #agregar la última página del archivo al merger 

        #merger.append(open(pdf, 'rb'), pages=(number_of_pages , number_of_pages))
        merger.append(pdf_reader, pages=(number_of_pages , (number_of_pages + 1)))

# eliminar la carpeta Temp
shutil.rmtree(temp)

# escribir el archivo pdf resultante
with open(Carpeta + '/Consolidado última Hoja.pdf', 'wb') as fout:
        merger.write(fout)
