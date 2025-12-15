from utils import script_exec, log
from modules import amass, ffuf, gau, httpx, nuclei, options, subfinder, sublister


Definitions = {
        "Create_project": options.Create_project,
        "Change_project": options.Change_project,
        "Delete_project": options.Delete_project,
        "Fetch_project": options.Fetch_project,

        "Custom_Header_Agent": options.Header_Agent,
    }
def handler(action, values=None):
    if action in Definitions:
        Definitions[action](values)