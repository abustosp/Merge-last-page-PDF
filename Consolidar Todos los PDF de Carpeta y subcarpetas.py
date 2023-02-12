import PyPDF2, os
from tkinter.filedialog import askdirectory
from PyPDF2 import PdfReader, PdfMerger

# Seleccionar la carpeta donde se encuentran los archivos PDF
folder = askdirectory() 
os.chdir(folder) 

# Obtener todos los archivos PDF de la carpeta Folder y sus subcarpetas
pdfFiles = []
for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfFiles.append(os.path.join(foldername, filename))

#pdfFiles.sort(key=str.lower) # Ordenar los archivos alfabéticamente 

#Ordenar los archivos alfabéticamente sin tener en cuenta el path
pdfFiles.sort(key=os.path.basename)

 # Crear el objeto PDF merger 
pdfMerger = PdfMerger() 

 # Añadir cada archivo PDF al objeto merger 
for filename in pdfFiles: 
    with open(filename, 'rb') as f: 
        pdf_reader = PdfReader(f)
        Number_of_pages = len(pdf_reader.pages) -1
        pdfMerger.append(pdf_reader , pages=(0, Number_of_pages + 1 ))

for i in range(len(pdfFiles)):
    #pdfMerger.add_outline_item(title=str(pdfFiles[i]), pagenum=i)
    #Agregar un marcador de página para cada archivo PDF sin el path
    pdfMerger.add_outline_item(title=str(os.path.basename(pdfFiles[i])), pagenum=i)

 # Escribir el contenido del merger en un nuevo archivo PDF 								  
with open('Consolidado IVA IIBB.pdf', 'wb') as f: 
    pdfMerger.write(f)