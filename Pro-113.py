import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "c://Users//comma//Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Olá, {event.src_path} foi excluído!")

    def on_modified(self, event):
        print(f"Olá, {event.src_path} foi modificado!")

    def on_moved(self, event):
        print(f"Olá, {event.src_path} foi movido para {event.dest_path}")
    

    #1_on_created

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("Executando...")
except KeyboardInterrupt:
        print("Interrompido!") 
        observer.stop()       







