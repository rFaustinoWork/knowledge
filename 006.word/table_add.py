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


doc.Paragraphs(doc.Paragraphs.Count).Range.InsertParagraphAfter()


print("Nb. of tables: ", doc.Bookmarks.Count)

table = doc.Tables.Add(doc.Paragraphs(doc.Paragraphs.Count).Range, 5, 2)

print("Nb. of tables: ", doc.Bookmarks.Count)


doc.Close()


