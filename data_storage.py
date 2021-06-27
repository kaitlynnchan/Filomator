import json
from json.decoder import JSONDecodeError

global json_file_name
json_file_name = "data.txt"

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

# def write_name(name):

# def write_time(hour, min, am_pm)

# def write_days_of_week(days_of_week)

# def write_source_folder(source_folder)

# def write_dest_folder(dest_folder)

# def write_desired_files(desired_files)

def write_data(name, hour, mins, days_of_week, source_folder, dest_folder, desired_files):
    data_string = '{ "' + name + '": { "time": { "hour":"' + hour + '", "min":"' + mins + '" }, "daysOfWeek":[], "sourcePath":"' + source_folder + '", "destPath":"' + dest_folder + '", "desiredFiles":[] } }'
    
    data_dict = json.loads(data_string)
    data_dict[name]["daysOfWeek"] = days_of_week
    data_dict[name]["desiredFiles"] = desired_files

    try:
        with open(json_file_name) as json_file:
            # load file and update json object with data
            json_object = json.load(json_file)
            json_object.update(data_dict)
    except (IOError, JSONDecodeError):
        # file is empty or does not exists
        # first entry
        json_object = data_dict

    with open(json_file_name, 'w') as json_file:
        # write new json object to file in nice format
        json.dump(json_object, json_file, indent = 4)

    print(json.dumps(json_object, indent = 4))

#def read_data()