import os
from PyPDF2 import PdfWriter

def mergeer():
    os.chdir(path)
    pdf_list = os.listdir()
    pdfs = []
    for pdf in pdf_list:
        if pdf.endswith(".pdf"):
            pdfs.append(pdf)
    print(pdfs)
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()

path = input("Enter the path of the Folder where pdfs are : ")
mergeer()
print("Your Merged PDF has been created.")

# --------------------------------------------------------------------
# Apply a Sorting function in it so you can merge as per your order.
# --------------------------------------------------------------------