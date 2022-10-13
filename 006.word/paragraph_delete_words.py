import win32com.client
from win32com.client import constants
from create_sample_doc import duplicate_sample_doc
import os

FILENAME = "dummy_file.docx"

# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdunits?view=word-pia
wdWord = 2

file_path = duplicate_sample_doc(FILENAME)

word = win32com.client.Dispatch("Word.Application")
word.visible = True

wb = word.Documents.Open(file_path)
doc = word.ActiveDocument


print(" Paragraph 1 content (original): ", doc.Paragraphs(1).Range.Text)

range = doc.Paragraphs(1).Range

range.Collapse(1)
range.Move(wdWord, 2)
range.MoveEnd(wdWord, 2)
range.Delete(wdWord, 1)

print(" Paragraph 1 content (updated): ", doc.Paragraphs(1).Range.Text)

print(" Paragraph 2 content (no change): ", doc.Paragraphs(2).Range.Text)

doc.Close()


