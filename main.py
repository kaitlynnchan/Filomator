from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import datetime
from datetime import date
from data_storage import *

# doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
# img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
# software_types = ('.exe', '.pkg', '.dmg')


# assumes at least one of the following arguments is unique:
#   time, days_of_week, source_path, desired_files
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        names = get_all_names()
        for name in names:
            src_path = get_entry_by_key(name, "sourcePath")
            start_time = get_entry_by_key(name, "startTime")
            end_time = get_entry_by_key(name, "endTime")
            days_of_week = get_entry_by_key(name, "daysOfWeek")

            # check if date matches
            now = datetime.datetime.now()
            result_between = self.is_in_between(now.time(), start_time.time(), end_time.time())

            delta_time = datetime.timedelta(days=result_between[1])
            date_calculated = date.today() + delta_time;
            if result_between[0] and result_between[1] == 0 \
                    and (date.today().weekday() in days_of_week):
                self.find_files(name, now, src_path)
            elif result_between[0] and result_between[1] == -1 \
                    and (date_calculated.weekday() in days_of_week):
                self.find_files(name, now, src_path)

    # determines if current time is in between start and end time
    # returns True or False, and how many days overnight
    def is_in_between(self, now, start_time, end_time):
        if start_time < end_time:
            print(" same day")
            return now >= start_time and now <= end_time, 0
        else:  # crosses midnight
            print("overnight")
            return now >= start_time or now <= end_time, -1

    def find_files(self, name, now, src_path):
        dest_path = get_entry_by_key(name, "destPath")
        desired_files = get_entry_by_key(name, "desiredFiles")
        new_file_name = get_entry_by_key(name, "newFileName")

        # look through all files at source path
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
                number_name = '/File-' + str((number_files + 1))
                new_name = new_path + number_name + str(file_extension)
                os.rename(source, new_name)


event_handler = Handler()
observer = Observer()

# initialize observer for each path
source_paths = extract_entries_by_key("sourcePath")
source_paths = list(set(source_paths))
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
