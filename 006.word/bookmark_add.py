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


print("Nb. of bookmarks: ", doc.Bookmarks.Count)

range = doc.Paragraphs(1).Range
doc.Bookmarks.Add("sampleBookmark", range.Words(6))

print("Nb. of bookmarks: ", doc.Bookmarks.Count)
print("Is \"sampleBookmark\" set?", doc.Bookmarks.Exists("sampleBookmark"))


doc.Close()


