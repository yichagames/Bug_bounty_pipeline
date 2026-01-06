from utils.log import log
from utils.script_exec import execute
from modules import amass, ffuf, gau, httpx, nuclei, options, subfinder, sublister


Definitions = {
    # amass

    # ffuf

    # gau

    # httpx

    # nuclei

    # options
    
    "Create_project": options.Create_project,
    "Delete_project": options.Delete_project,
    "Current_project": options.Current_project,
    "Fetch_all_projects": options.Fetch_all_projects,
    "Fetch_project": options.Fetch_project,
    "Change_project": options.Change_project,

    "Custom_Header_Agent": options.Header_Agent,
    
    # subfinder
    "Subfinder_scan": subfinder.subfinder_scan,

    # sublister

    }
def handler(action, values=None):
    if action in Definitions:
        return Definitions[action](values)
