#first install PYPDF2 library
from PyPDF2 import PdfFileReader, PdfFileWriter
pdffilepath = 'file1.pdf' #download pdf file
pdf = PdfFileReader(pdffilepath)

pages = [0, 2, 4] #page 1, 3 and 5
pdfwriter = PdfFileWriter()

for pagenum in pages:
    pdfwriter.addPage(pdf.getPage(pagenum)) #gets content from each pages, add them in pdfwriter

with open ('output.pdf', 'wb') as out:
    pdfwriter.write(out) #creates output file
print("PDF file has been split!")