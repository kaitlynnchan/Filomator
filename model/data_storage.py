import json
from json.decoder import JSONDecodeError
import datetime
from datetime import date
from sys import argv
import string

# JSON format
#     {
#         "name": {
#             "startTime":"", (HH:MM)
#             "endTime":"",   (HH:MM)
#             "daysOfWeek":[], monday = 0, sunday = 6
#             "sourcePath":"",
#             "destPath":"",
#             "desiredFiles":[],
#             "newFileName": ""
#         }
#     }

global json_file
json_file = "../assets/data.json"


def convert_to_24_hr_clock(hour, is_time_pm):
    if (not hour) or (hour is None) or (is_time_pm is None) or (not is_time_pm):
        print("Parameters are not valid")

    hour = int(hour)
    if is_time_pm == 'PM' and 0 < hour <= 12:
        # convert time to 24 hour clock
        hour += 12
    # if is_time_pm and 0 < hour <= 12:
    #     # convert time to 24 hour clock
    #     hour += 12
    return str(hour)


# convert hour and mins to datetime before calling write
def convert_to_datetime(hour, mins):
    if (not hour) or (hour is None) or (not mins) or (mins is None):
        print("Parameters are not valid")
    return datetime.time(int(hour), int(mins))


# calculates end time from start time and delta time
def calculateEndTime(start_time):
    # converts start_time to datetime object
    start_datetime = datetime.datetime.combine(datetime.date.today(), start_time)
    delta_time = datetime.timedelta(minutes=10)

    # set end_time to delta time ahead
    end_datetime = start_datetime + delta_time
    end_time = end_datetime.time()
    return end_time


def write_to_json(name, start_time, end_time, days_of_week, source_path, dest_path, desired_files, new_file_name):
    if (not name) or (name is None) \
            or (not start_time) or (start_time is None) \
            or (not end_time) or (end_time is None) \
            or (not days_of_week) or (days_of_week is None) \
            or (not source_path) or (source_path is None) or (not dest_path) or (dest_path is None) \
            or (not desired_files) or (desired_files is None)\
            or (not new_file_name) or (new_file_name is None):
        print("All fields must be filled")
        return

    # convert to string
    start_time_str = start_time.strftime("%H:%M")
    end_time_str = end_time.strftime("%H:%M")

    data_dict = {
        name: {
            "startTime": start_time_str,
            "endTime": end_time_str,
            "daysOfWeek": [],
            "sourcePath": source_path,
            "destPath": dest_path,
            "desiredFiles": [],
            "newFileName": new_file_name
        }
    }
    data_dict[name]["daysOfWeek"] = [days_of_week]
    data_dict[name]["desiredFiles"] = [desired_files]

    try:
        with open(json_file) as file:
            # load file and update json object with data
            json_object = json.load(file)
            json_object.update(data_dict)
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        # first entry
        json_object = data_dict

    with open(json_file, 'w') as file:
        # write new json object to file in nice format
        json.dump(json_object, file, indent=4)

    print(json.dumps(json_object, indent=4))


def extract_data_fr_json():
    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)
            # print(json.dumps(json_object, indent=4))
            print("extracted data")
            return json_object
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        # first entry
        print("File is not accessible")
        return None


def extract_entry(name):
    if name is None:
        print("Entry cannot be null")
        return None

    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            # check if entry is in json object
            if name in json_object:
                # get entry at name
                entry = json_object[name]
                print(json.dumps(entry, indent=4))
                return entry
            else:
                print("Entry '" + name + "' was not found")
                return None
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None


def extract_entries_by_key(key_name):
    if key_name is None:
        print("Argument cannot be null")
        return None

    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            # get all values in key for each element
            key_values = []
            for name in json_object:
                key_values.append(json_object[name][key_name])

            print(key_values)
            return key_values
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None


def get_entry_by_key(name, key):
    if (key is None) or (name is None):
        print("Argument cannot be null")
        return None

    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            if name in json_object:
                if (key == "startTime") or (key == "endTime"):
                    return datetime.datetime.strptime(json_object[name][key], "%H:%M")
                # get key for name
                return json_object[name][key]
            else:
                print("Entry '" + name + "' was not found")
                return None
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None


def get_all_names():
    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            return json_object.keys()
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None


if __name__ == '__main__':
    # parse argument array
    time = argv[2].strip("[]")
    time = time.split(",")
    for i in range(len(time)):
        time[i] = time[i].strip('\'')
    hour = convert_to_24_hr_clock(time[0], time[2])
    start_time = convert_to_datetime(hour, time[1])
    end_time = calculateEndTime(start_time)

    # parse argument array
    week = argv[3].strip('[]')
    week = week.split(",")
    for i in range(len(week)):
        week[i] = week[i].strip('\'')
        week[i] = int(week[i])

    # parse argument array
    files = argv[6].strip('[]')
    files = files.split(",")
    for i in range(len(files)):
        files[i] = files[i].strip('\'')

    write_to_json(argv[1].strip('\''), start_time, end_time, week, argv[4].strip('\''), argv[5].strip('\''), files, argv[7].strip('\''))