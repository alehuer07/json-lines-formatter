from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import jsonlines
import json
import os
import time

# Global Variables
FOLDER_TO_TRACK = "C:/Users/alehu/Desktop/JSON_Input/"
JSON_FOLDER_DESTINATION = "C:/Users/alehu/Desktop/JSON_Output/"
JSONLINES_FOLDER_DESTINATION = "C:/Users/alehu/Desktop/JSONLINES_Output/"


# Automation Event Handler
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            src = FOLDER_TO_TRACK + "/" + filename
            json_new_destination = JSON_FOLDER_DESTINATION + "/" + filename

            # Change file extension from json to jl
            base = os.path.splitext(filename)[0]
            jsonlines_new_destination = JSONLINES_FOLDER_DESTINATION + base + ".jl"

            self.changeFormatting(src, jsonlines_new_destination)

            os.rename(src, json_new_destination)

    def changeFormatting(self, fileToConvert, newDestination):
        with open(fileToConvert, "r") as f:
            json_data = json.load(f)

        with jsonlines.open(newDestination, "w") as writer:
            writer.write_all(json_data)


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
