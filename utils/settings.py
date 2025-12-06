import log
import json
import traceback

def read_setting(key):
    try: 
        with open("config.json", "r") as f:
            data = json.load(f)
        for k in key:
            data = data[k]
        return data
    except:
        log.log(f"Error while reading settings: {traceback.format_exc()}", "warning")
        return

def write_setting(key, value):
    try: 
        with open("config.json", "r") as f:
            data = json.load(f)
        d = data
        for k in key[:-1]:
            d = d[k]
        d[key[-1]] = value
        with open("config.json", "w") as f:
            json.dump(data, f, indent=4)
        log.log(f"Successfully wrote {d[key[-1]]} into {d}")
    except:
        log.log(f"Error while writing settings: {traceback.format_exc_exc()}", "warning")
        return