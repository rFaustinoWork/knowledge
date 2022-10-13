import enum
import win32com.client
from win32com.client import constants
from create_sample_doc import duplicate_sample_doc
import os

FILENAME = "dummy_file.docx"

# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdcolorindex?view=word-pia
wdDarkYellow = 14
wdTurquoise = 3

file_path = duplicate_sample_doc(FILENAME)

word = win32com.client.Dispatch("Word.Application")
word.visible = True

wb = word.Documents.Open(file_path)
doc = word.ActiveDocument


table = doc.Tables(1)

print("----------------")
print("Nb. rows (original): ", table.Rows.Count)
for i, r in enumerate(table.Rows):
    print("row", i, ":", r.Cells(1).Range.Text[:-2])

print("----------------")
print("Add row at the end of the table")
row = table.Rows.Add()
row.Cells(1).Range.InsertAfter("LastRow(3,1)")

print("Nb. rows (updated): ", table.Rows.Count)
for i, r in enumerate(table.Rows):
    print("row", i, ":", r.Cells(1).Range.Text[:-2])

print("----------------")
print("Add row before row 2")
row = table.Rows.Add(table.Rows(2))
row.Cells(1).Range.InsertAfter("MiddleRow(2,1)")

print("Nb. rows (updated): ", table.Rows.Count)
for i, r in enumerate(table.Rows):
    print("row", i, ":", r.Cells(1).Range.Text[:-2])

doc.Close()


