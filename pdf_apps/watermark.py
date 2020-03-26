from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

input = PdfFileReader(open('./pdfs/simple.pdf', 'rb'))
watermark = PdfFileReader(open('./pdfs/watermark.pdf', 'rb'))
output = PdfFileWriter()

for i in range(input.getNumPages()):
    page = input.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('result.pdf', 'wb') as result_file:
    output.write(result_file)
