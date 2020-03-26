from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

with open('./pdfs/dummy.pdf', 'rb') as file:
    reader = PdfFileReader(file)
    page = reader.getPage(0)

    writer = PdfFileWriter()

    writer.addPage(page.rotateClockwise(180))
    with open('tilt.pdf', 'wb') as wfile:
        writer.write(wfile)
