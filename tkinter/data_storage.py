import json
from json.decoder import JSONDecodeError

# JSON format
#     {
#         "name": {
#             "time": {
#                 "hour":"",
#                 "min":""
#             }, (24 hr format)
#             "days_of_week":[],
#             "source_path":"",
#             "dest_path":"",
#             "desired_files":[],
#             "newFileName": ""
#         }
#     }

global json_file
json_file = "../data.json"


def convert_to_24_hr_clock(hour, is_time_pm):
    if (not hour) or (hour is None) or (is_time_pm is None) or (not is_time_pm):
        print("Parameters are not valid")

    hour = int(hour)
    if is_time_pm and 0 < hour <= 12:
        # convert time to 24 hour clock
        hour += 12
    return str(hour)


def write_to_json(name, hour, mins, days_of_week, source_path, dest_path, desired_files, new_file_name):
    if (not name) or (name is None) \
            or (not hour) or (hour is None) or (int(hour) == 0) or (not mins) or (name is mins) \
            or (not days_of_week) or (days_of_week is None) \
            or (not source_path) or (source_path is None) or (not dest_path) or (dest_path is None) \
            or (not desired_files) or (desired_files is None)\
            or (not new_file_name) or (new_file_name is None):
        print("All fields must be filled")
        return

    data_dict = {
        name: {
            "time": {
                "hours": hour,
                "mins": mins
            },
            "daysOfWeek": [],
            "sourcePath": source_path,
            "destPath": dest_path,
            "desiredFiles": [],
            "newFileName": new_file_name
        }
    }
    data_dict[name]["daysOfWeek"] = days_of_week
    data_dict[name]["desiredFiles"] = desired_files

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
            print(json.dumps(json_object, indent=4))
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


def extract_entry_by_key(key):
    if key is None:
        print("Argument cannot be null")
        return None

    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            for key, value in json_object.items():
                pprint("Key:")
                pprint(key)

            # check if entry is in json object
            # if name in json_object:
            #     # get entry at name
            #     entry = json_object[name]
            #     print(json.dumps(entry, indent=4))
            #     return entry
            # else:
            #     print("Entry '" + name + "' was not found")
            #     return None
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None
