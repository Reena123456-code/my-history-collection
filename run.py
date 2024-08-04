import pandas as pd 

def read_html_with_read_html(file_path):
    df = pd.read_html(file_path)[0]
    df =read_html_with_read_html(html_file_path)

    print("Approach 1 Output:")
    print(df)


import csv
from tkinter import *
from tkinter import messagebox

#function to add a book to the library
def add_book():
    box_no = box_no_entry.get()
    book_subject = book_subject_entry.get()
    book_id =book_id_entry.get()
    book_author = book_author_entry.get()
    book_title = book_title_entry.get()

import nfc
import ndef
from threading import Thread

