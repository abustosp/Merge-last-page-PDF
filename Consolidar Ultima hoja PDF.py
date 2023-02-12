import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from tkinter.filedialog import askdirectory
import shutil

# Preguntar por la ruta de la carpeta
Carpeta = askdirectory(title='Seleccionar carpeta')

# especificar la ruta de la carpeta
Fp1 = Carpeta + "/RI"
Fp2 = Carpeta + "/M"

#Listar todos los archivos de las carpetas 'RI' y 'M' 
# listar todos los archivos pdf en la carpeta
pdf_files1 = [f for f in os.listdir(Fp1) if f.endswith(".pdf")]
pdf_files2 = [f for f in os.listdir(Fp2) if f.endswith(".pdf")]

#Agregar el Path de cada archivo
pdf_files1 = [Fp1 + "/" + f for f in pdf_files1]
pdf_files2 = [Fp2 + "/" + f for f in pdf_files2]

#unir las listas pdf_files1 y pdf_files2
pdf_files = pdf_files1 + pdf_files2

#ordenar pdf_files por nombre
#pdf_files.sort()

temp = Carpeta + "/Temp"

# Crear carpeta Temp
if not os.path.exists(temp):
    os.makedirs(temp)

#Copiar los archivos de pdf_files a la carpeta Temp
for pdf in pdf_files:
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
with open('Consolidado Libros Compras Ventas.pdf', 'wb') as fout:
        merger.write(fout)
