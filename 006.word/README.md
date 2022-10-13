# Word Object Model

See [Word object model overview](https://learn.microsoft.com/en-us/visualstudio/vsto/word-object-model-overview?view=vs-2022&tabs=csharp)

See [Python for Win32 Extensions Help](https://mhammond.github.io/pywin32/)

See [Win32Com](https://win32com.goermezer.de/category/microsoft/ms-office)

## Dependencies
- [pywin32](https://pypi.org/project/pywin32/)


## Create and Save new document.
- [New document](app_new_document.py)
- [Sample file generation](create_sample_doc.py)

## How to handle paragraphs?
- [read](paragraph_read.py)
- [insert after](paragraph_insert_after.py)
- [insert middle](paragraph_insert_middle.py)
- [delete word in 3rd position](paragraph_delete_words.py) - removes the third word in the first paragraph.
- [delete specific word](paragraph_delete_specific_word.py) - removes the *paragraph* word present in the first paragraph.
- [highligh text](paragraph_highlight.py) - word *first* is highlighted
- [change font](paragraph_font_change.py) - words *first* and *document* highlighted with different font color, font name and font size.

## How to handle bookmarks?
- [insert cross reference](bookmark_insert.py)
- [create](bookmark_add.py)

## How to handle tables?
- [create](table_add.py)
- [read cells value](table_read.py)
- [highlight cell](table_highlight.py) - highlights cell (1,2) and (2,1)
- [add row](table_add_row.py)

## How to handle comments?
- [export comments](comments_export.py)

