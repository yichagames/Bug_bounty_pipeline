from utils.log import log
from utils.script_exec import execute
from utils.settings import write_settings, read_settings, delete_settings
from modules import options

def subfinder_scan(p = None):
    domain = options.Current_project()
    execute((["subfinder", "-d", domain, "--silent", "-o", "./outputs/subfinder_"+domain+".txt"]))