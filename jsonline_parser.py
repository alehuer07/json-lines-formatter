from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import jsonlines
import json
import os
import time

# Global Variables
FOLDER_TO_TRACK = "C:/Users/alehu/Desktop/JSON_Input/"
FOLDER_DESTINATION = "C:/Users/alehu/Desktop/JSONLINES_Output/"


# Automation Event Handler
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):

            src = FOLDER_TO_TRACK + "/" + filename
            new_destination = FOLDER_DESTINATION + "/" + filename

            changeFormatting(src, new_destination)

            file_done = False
            file_size = -1

            # os.rename(src, new_destination)


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()


def changeFormatting(fileToConvert, newFileName):
    # x = input("Type in the name of a file you want to convert: ")
    # fileToConvert = "./" + x

    with open(fileToConvert, "r") as f:
        json_data = json.load(f)

    with jsonlines.open(newFileName, "w") as writer:
        writer.write_all(json_data)