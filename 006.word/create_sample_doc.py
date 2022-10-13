import win32com.client
from win32com.client import constants
import os
import shutil

FILENAME = "sample_doc.docx"
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, FILENAME)


def duplicate_sample_doc(new_file_name):
    new_file_name_dir = os.path.join(BASE_DIR, new_file_name)
    
    if os.path.exists(new_file_name_dir):
        os.remove(new_file_name_dir)
    
    if not os.path.exists(FILE_PATH):
        create_new_sample_doc()
    
    shutil.copy(FILE_PATH, new_file_name_dir)
    return new_file_name_dir


def create_new_sample_doc():
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

    word = win32com.client.Dispatch("Word.Application")
    word.visible = True

    # Create a new file
    print("Creating a new sample file...", end='')
    wb = word.Documents.Add()
    doc = word.ActiveDocument

    p1 = doc.Paragraphs(1)
    r1 = p1.Range
    r1.End -= 1
    r1.InsertAfter("The first paragraph of the document.")

    r1.InsertParagraphAfter()
    r1.InsertAfter("A second paragraph.")
    r1.InsertParagraphAfter()
    r1.InsertParagraphAfter()

    # Add a table with 2 rows and 3 columns
    table = doc.Tables.Add(doc.Paragraphs(3).Range, 2, 3)

    table.Rows(1).Cells(1).Range.InsertAfter("R1 C1")
    table.Rows(1).Cells(2).Range.InsertAfter("R1 C2")
    table.Rows(1).Cells(3).Range.InsertAfter("R1 C3")

    table.Rows(2).Cells(1).Range.InsertAfter("R2 C1")
    table.Rows(2).Cells(2).Range.InsertAfter("R2 C2")
    table.Rows(2).Cells(3).Range.InsertAfter("R2 C3")

    # Change row 2 cell 3 style
    r2c3 = table.Rows(2).Cells(3).Range
    r2c3.Bold = True
    r2c3.Font.Color = 0xBB0000
    r2c3.Font.Name = "Verdana"
    r2c3.Font.Size = 16


    doc.SaveAs(FILE_PATH)
    doc.Close()

    print("done")

if __name__ == "__main__":
    create_new_sample_doc()
