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

table.Rows(1).Cells(2).Range.HighlightColorIndex = wdDarkYellow
table.Rows(2).Cells(1).Range.HighlightColorIndex = wdTurquoise

doc.Close()


