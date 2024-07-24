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
