import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Apple/Downloads"

#Event Handler Class
class FileMovementHandler(FileSystemEventHandler):
    # code to handle new file creation event in a directory
    # on_any_event()

    # on_created()
    def on_created(self,event):
        print(event)

    # on_modified()
    # on_moves()
    # on_deleted()


#initialize event handler class
event_handler = FileMovementHandler()

#initialize observer
observer = Observer()

#schedule the observer
observer.schedule(event_handler, from_dir, recursive=True)

#start the observer
observer.start()

while True:
    time.sleep(2)
    print("running...")

#exceptions - 1) Built-in  2) User-defined