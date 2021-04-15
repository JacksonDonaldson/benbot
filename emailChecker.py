import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import importlib
import time
import dataStorage

username = dataStorage.email;
password = dataStorage.emailPassword;

def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

def checkMostRecentEmail():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    imap.login(username,password)

    status, messages = imap.select()

    messages = int(messages[0])
    print(messages)
