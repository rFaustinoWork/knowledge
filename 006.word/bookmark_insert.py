import win32com.client
from win32com.client import constants
from create_sample_doc import duplicate_sample_doc
import os

FILENAME = "dummy_file.docx"

# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdreferencetype?view=word-pia
wdRefTypeBookmark = 2
#https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdreferencekind?view=word-pia
wdContentText = -1

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

print(" Paragraph 2 content (original): ", doc.Paragraphs(2).Range.Text)

range = doc.Paragraphs(2).Range
range.End -= 1
range.InsertAfter(" in the ")
range = doc.Paragraphs(2).Range
range.End -= 1
range.Start = range.End
range.InsertCrossReference(wdRefTypeBookmark, wdContentText, "sampleBookmark", True)

print(" Paragraph 2 content (updated): ", doc.Paragraphs(2).Range.Text)



doc.Close()


