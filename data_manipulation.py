import pandas as pd
from data_storage import *
from datetime import date
import datetime
import time

global data_frame

def identify_overnight():
    data_frame.loc[data_frame["startTime"] < data_frame["endTime"], "overnight"] = False
    data_frame.loc[data_frame["startTime"] >= data_frame["endTime"], "overnight"] = True
    print(data_frame)
    #convert times to datetimes


def correct_times(time, day):
    # df = data_frame[(pd.to_datetime(data_frame["startTime"]).dt.time <= time
    #                  <= pd.to_datetime(data_frame["endTime"]).dt.time
    #                  and not data_frame['overnight'])
    #                 | (time >= pd.to_datetime(data_frame['startTime']).dt.time
    #                    | time <= pd.to_datetime(data_frame['endTime']).dt.time
    #                    and data_frame['overnight'])]
    df = data_frame.query("(pd.to_datetime(data_frame['startTime']).dt.time <= time) & (time <= pd.to_datetime(data_frame['endTime']).dt.time)")
    # df = data_frame[(pd.to_datetime(data_frame["startTime"]).dt.time <= time)]
    print(df)
    # if(df["overnight"] and time <= data_frame["endTime"]):
    #     delta_time = datetime.timedelta(days=-1)
    #     day = day + delta_time
    # check if day matches
    # print(df)



data_frame = pd.read_json(json_file)
data_frame = data_frame.transpose()
identify_overnight()
    # data_frame.replace(to_replace="endTime", value=pd.to_datetime(data_frame["endTime"]).dt.time, inplace=True)
    #pd.to_datetime(data_frame["endTime"]).dt.time
#pd.to_datetime(data_frame["startTime"], "%H:%M").time()
#start_time.strftime("%H:%M")
tim = datetime.time(10, 0)
correct_times(tim, date.today())