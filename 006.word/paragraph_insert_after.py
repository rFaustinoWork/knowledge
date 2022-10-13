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


print(" Paragraph 1 content (original): ", doc.Paragraphs(1).Range.Text)

range = doc.Paragraphs(1).Range
# adjusting the end of the range to exclude the '\n' (new line character)
range.End -= 1
range.InsertAfter("NEW TEXT")

print(" Paragraph 1 content (updated): ", doc.Paragraphs(1).Range.Text)

print(" Paragraph 2 content (no change): ", doc.Paragraphs(2).Range.Text)

doc.Close()


