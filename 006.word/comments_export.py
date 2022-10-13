import enum
import win32com.client
from create_sample_doc import duplicate_sample_doc
import os

FILENAME = "comments_file.docx"
BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, FILENAME)

# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdgotodirection?view=word-pia
wdGoToAbsolute = 1
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdgotoitem?view=word-pia
wdGoToComment = 6
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdunits?view=word-pia
wdParagraph = 4
# https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.word.wdinformation?view=word-pia
wdActiveEndPageNumber = 3

if not os.path.exists(FILE_PATH):
    print(FILENAME+" not found.")
    exit(1)


word = win32com.client.Dispatch("Word.Application")
word.visible = True

wb = word.Documents.Open(FILE_PATH)
doc = word.ActiveDocument


for c in doc.Comments:
    # if c.Ancestor is None and len(c.Replies) == 0:  
        
    r = doc.GoTo(wdGoToComment, wdGoToAbsolute, c.Index)
    r.Expand(wdParagraph)
    page = r.Information(wdActiveEndPageNumber)
    
    print("---------------------------------")
    print("Index     : ", c.Index)
    print("Page      : ", str(page))
    print("Author    : ", c.Author)
    print("Comment   : ", c.Range.Text)
    print("Regarding : ", c.Scope.Text)
    print("Regarding (paragraph) : ", r.Text)

doc.Close()



   
