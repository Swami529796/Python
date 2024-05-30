from PyPDF2 import PdfFileReader, PdfFileWriter

pages = [0,2]
with open ("Policy.pdf","rb") as f:
    reader = PdfFileReader(f)
    writer = PdfFileWriter()
    rest_writer = PdfFileWriter()

    for page in range(len(reader.pages)):
        if page in pages:
            writer.addPage(reader.getPage(page))
        else:
            rest_writer.addPage(reader.getPage(page))

    with open("selected.pdf", "wb") as f2:
        writer.write(f2)

    with open("rest.pdf", "wb") as f2:
        rest_writer.write(f2)
print('Done')

        