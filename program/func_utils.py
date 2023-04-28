from datetime import datetime, timedelta
# format number function
def format_number(curr_num, match_num):

  """
  give current number with desired decimals
  function will return the correctly formatted string
  
  """
  curr_num_string=f"{curr_num}"
  match_num_string=f"{match_num}"

  if "." in match_num_string:
    match_decimals = len(match_num_string.split(".")[1])
    curr_num_string = f"{curr_num:.{match_decimals}f}"
    curr_num_string = curr_num_string[:]
    return curr_num_string
  else:
    return f"{int(curr_num)}"
  



# format time
def format_time(timestamp):
  return timestamp.replace(microsecond=0).isoformat()



# get iso times
def get_ISO_time():
  
  # get time stamps ( try to do a while loop later on after this is confirmed to be working )
  date_start_0 = datetime.now()
  date_start_1 = date_start_0 - timedelta(hours=100)
  date_start_2 = date_start_1 - timedelta(hours=100) 
  date_start_3 = date_start_2 - timedelta(hours=100)  
  date_start_4 = date_start_3 - timedelta(hours=100)

  # format datetimes
  times_dict = {
    "range1":{
      "from_iso": format_time(date_start_1),
      "to_iso": format_time(date_start_0),
    },
    "range2":{
      "from_iso": format_time(date_start_2),
      "to_iso": format_time(date_start_1),
    },
 
    "range3":{
      "from_iso": format_time(date_start_3),
      "to_iso": format_time(date_start_2),
    },
    "range4":{
      "from_iso": format_time(date_start_4),
      "to_iso": format_time(date_start_3),
    }
  }

  # return results
  return times_dict