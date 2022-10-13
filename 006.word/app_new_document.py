import win32com.client
from win32com.client import constants
import os

FILENAME = "testFile.docx"
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, FILENAME)

if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)


word = win32com.client.Dispatch("Word.Application")
word.visible = True

# Create a new file
wb = word.Documents.Add()
doc = word.ActiveDocument

# save the new file with name "testFile.docx"
doc.SaveAs(FILE_PATH)
