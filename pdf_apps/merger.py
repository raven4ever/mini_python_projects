from PyPDF2 import PdfFileMerger
import sys

inputs = sys.argv[1:]


def pdf_combiner(file_list):
    merger = PdfFileMerger()

    for pdf_file in file_list:
        print(pdf_file)
        merger.append(pdf_file)

    merger.write('super_pdf.pdf')


pdf_combiner(inputs)
