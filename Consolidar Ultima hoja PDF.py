import os
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# especificar la ruta de la carpeta
Fp1 = "RI"
Fp2 = "M"

#Listar todos los archivos de las carpetas 'RI' y 'M' 
# listar todos los archivos pdf en la carpeta
pdf_files1 = [f for f in os.listdir(Fp1) if f.endswith(".pdf")]
pdf_files2 = [f for f in os.listdir(Fp2) if f.endswith(".pdf")]

#unir las listas pdf_files1 y pdf_files2
pdf_files = pdf_files1 + pdf_files2

#ordenar pdf_files por nombre
pdf_files.sort()

# agregar la ruta completa a cada archivo pdf
pdf_files = ["Temp" + "/" + pdf for pdf in pdf_files]

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


# escribir el archivo pdf resultante
with open('Consolidado Libros Compras Ventas.pdf', 'wb') as fout:
        merger.write(fout)
