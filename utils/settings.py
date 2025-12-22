import json, traceback
from utils.log import log

def read_settings(key):
    try: 
        with open("config.json", "r") as f:
            data = json.load(f)
        for k in key:
            if k not in data:
                return f"{k} in {key} not found"
            data = data[k]
        return data
    except:
        log(f"Error while reading settings: {traceback.format_exc()}", "warning")
        return

def write_settings(key, value):
    try: 
        with open("config.json", "r") as f:
            data = json.load(f)
        d = data
        for k in key[:-1]:
            if k not in d:
                d[k] = {}
            d = d[k]
        d[key[-1]] = value
        with open("config.json", "w") as f:
            json.dump(data, f, indent=4)
        log(f"Successfully wrote {d[key[-1]]} into {d}")
    except:
        log(f"Error while writing settings: {traceback.format_exc()}", "warning")
        return
    
def delete_settings(key):
    try: 
        with open("config.json", "r") as f:
            data = json.load(f)
        d = data
        for k in key[:-1]:
            if k not in d:
                log(f"Trying to delete a non-existing setting or a setting from a non-existing path")
                d[k] = {}
            d = d[k]
        del d[key[-1]]
        with open("config.json", "w") as f:
            json.dump(data, f, indent=4)
        log(f"Successfully removed a setting")
    except:
        log(f"Error while writing settings: {traceback.format_exc()}", "warning")
        return