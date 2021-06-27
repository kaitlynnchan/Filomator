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
#             "desired_files":[]
#         }
#     }

global json_file
json_file = "data.txt"

def convert_to_24_hr_clock(hour, is_time_pm):
    hour = int(hour)
    if is_time_pm and 0 < hour <= 12:
        # convert time to 24 hour clock
        hour += 12
    return str(hour)

def write_to_json(name, hour, mins, days_of_week, source_path, dest_path, desired_files):
    data_dict = { 
        name: {
            "time": {
                "hours": hour,
                "mins": mins
            },
            "daysOfWeek": [],
            "sourcePath": source_path,
            "destPath": dest_path,
            "desiredFiles": []
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
        json.dump(json_object, file, indent = 4)

    print(json.dumps(json_object, indent = 4))

def extract_data_fr_json():
    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)
            print(json.dumps(json_object, indent = 4))
            return json_object
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        # first entry
        print("File is not accessible")
        return None

def extract_entry(name):
    if name is None:
        return None

    try:
        with open(json_file) as file:
            # load file
            json_object = json.load(file)

            # check if entry is in json object
            if name in json_object:
                # get entry at name
                entry = json_object[name]
                print(json.dumps(entry, indent = 4))
                return entry
            else:
                print("Entry '" + name + "' was not found")
                return None
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        print("File is not accessible")
        return None