from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import datetime
from datetime import date

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

global current_hour, current_minute, current_date
now = datetime.datetime.now()
current_hour = now.hour
current_minute = now.minute
current_date = date.today()

global f_name
f_name = f"Screen Shot "


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(tracker):
            source = tracker + '/' + file
            file_name = os.path.splitext(source)[0]
            file_extension = os.path.splitext(source)[1]

            if f_name in file_name:
                if current_hour < 12:
                    new_path = destination + '/' + str(current_date) + "-" + str(current_hour) + "AM"
                else:
                    new_path = destination + '/' + str(current_date) + "-" + str(current_hour) + "PM"
                os.makedirs(new_path, exist_ok=True)

                number_files = len(os.listdir(new_path))
                new = new_path + '/File-' + str((number_files+1)) + str(file_extension)
                os.rename(source, new)


tracker = '/Users/sahaj/Desktop/SC1'
destination = '/Users/sahaj/Desktop/SC2'
# if current_hour == 3:
#     destination = '/Users/sahaj/Desktop/SC2'
# elif current_hour == 4:
#     destination = '/Users/sahaj/Desktop/SC3'
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, path=tracker, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
