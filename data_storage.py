import json
from json.decoder import JSONDecodeError

global json_file
json_file = "data.txt"

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

#def read_data()