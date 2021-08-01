from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import datetime
from datetime import date
from data_storage import *

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

# now = datetime.datetime.now()
# current_hour = now.hour
# current_minute = now.minute
# current_date = date.today()

# global f_name
# f_name = f"Screen Shot "


# assumes at least one of the following arguments is unique:
#   time, days_of_week, source_path, desired_files
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        data = extract_data_fr_json()
        for name in data:
            src_path = data[name]["sourcePath"]
            hours = data[name]["time"]["hours"]
            mins = data[name]["time"]["mins"]
            days_of_week = data[name]["daysOfWeek"]

            now = datetime.datetime.now()
            # and (now.minute >= mins)  and (date.today().weekday() in days_of_week)
            if (now.hour == int(hours)) and (now.minute >= int(mins)) \
                    and (date.today().weekday() in days_of_week):
                self.find_files(data, name, now, src_path)

    def find_files(self, data, name, now, src_path):
        dest_path = data[name]["destPath"]
        desired_files = data[name]["desiredFiles"]
        new_file_name = data[name]["newFileName"]

        for file in os.listdir(src_path):
            source = src_path + '/' + file
            file_name = os.path.splitext(source)[0]
            file_extension = os.path.splitext(source)[1]

            # check for name or extension in desired files
            if (file_extension in desired_files) or (file_name in desired_files):
                am_pm = "AM"
                if now.hour > 12:
                    am_pm = "PM"

                # move file
                new_path = dest_path + '/' + str(date.today()) + "-" + str(now.hour) + am_pm
                os.makedirs(new_path, exist_ok=True)

                # rename files
                number_files = len(os.listdir(new_path))
                new = new_path + '/File-' + str((number_files + 1)) + str(file_extension)
                os.rename(source, new)


# path_file = open('path.txt', 'r')
# tracker_paths = path_file.readline()
# tracker = '/Users/kaitl'
# path_file = open('path_destination.txt', 'r')
# destination_paths = path_file.readline()
# destination = '/Users/kaitl/Downloads/test'
# if current_hour == 3:
#     destination = '/Users/sahaj/Desktop/SC2'
# elif current_hour == 4:
#     destination = '/Users/sahaj/Desktop/SC3'


event_handler = Handler()
observer = Observer()

source_paths = extract_entry_by_key("sourcePath")
for path in source_paths:
    print(path)
    observer.schedule(event_handler, path=path, recursive=True)
observer.start()
print("observer start")


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
