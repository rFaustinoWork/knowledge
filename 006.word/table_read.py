import enum
import win32com.client
from win32com.client import constants
from create_sample_doc import duplicate_sample_doc
import os

FILENAME = "dummy_file.docx"

file_path = duplicate_sample_doc(FILENAME)

word = win32com.client.Dispatch("Word.Application")
word.visible = True

wb = word.Documents.Open(file_path)
doc = word.ActiveDocument


table = doc.Tables(1)

for idx_row, row in enumerate(table.Rows):
    for idx_cel, cell in enumerate(row.Cells):
        print("row: ", idx_row, "|col: ", idx_cel, "|value: ", cell.Range.Text[:-2])

doc.Close()


