#first install PYPDF2 library
from PyPDF2 import PdfFileReader, PdfFileWriter
pdffilepath = 'file1.pdf' #download pdf file
pdf = PdfFileReader(pdffilepath)

pdfwriter = PdfFileWriter()

for pagenum in range(2,6): #pages 2 thru 6
    pdfwriter.addPage(pdf.getPage(pagenum)) #gets content from each pages, add them in pdfwriter

with open ('newoutput.pdf', 'wb') as out:
    pdfwriter.write(out) #creates output file
print("PDF file has been split!")