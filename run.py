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

def beam(11c):
    snep_client = nfc.snep.SnepClient(11c)
    snep-client.put_records([ndef.UrlRecord('http://nfcpy.org')])

def connected(11c):
    Thread(target-beam, args=(11c,)).start()
    return True

with nfc.ContactlessFrontend('usb') as clf:
    clf.connect(11cp={'on-connect': connected})
