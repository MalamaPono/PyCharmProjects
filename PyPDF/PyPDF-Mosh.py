import PyPDF2

# altering and rotating pdf
# with open("PDF Files/first.pdf","rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated.pdf","wb") as output:
#         writer.write(output)

# combining PDFs
merger = PyPDF2.PdfFileMerger()
file_names = ["PDF Files/first.pdf","PDF Files/second.pdf"]
for file_name in file_names:
    merger.append(file_name)
merger.write("combined.pdf")
