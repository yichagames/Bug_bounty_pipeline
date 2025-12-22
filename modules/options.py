from utils.log import log
from utils.script_exec import execute
from utils.settings import write_settings, read_settings, delete_settings

def Create_project(p):
    log(f"Creating project {p["project_domain"]}")
    if p["project_domain"] in Fetch_all_projects():
        log(f"Trying to create an already existing project. Exiting...")
        return
    write_settings(["Projects", p["project_domain"]], {})
    log(f"Successfully created project {p["project_domain"]}")
    return

def Delete_project(p):
    log(f"Deleting project {p["project_domain"]}")
    delete_settings(["Projects", p["project_domain"]])
    log(f"Successfully deleted {p["project_domain"]} from projects")
    return

def Current_project(p):
    return read_settings(["Settings", "Current_project"])

def Fetch_all_projects(p):
    return list(read_settings(["Projects"]).keys())

def Fetch_project(p):
    return read_settings(["Projects", Current_project()])

def Change_project(p):
    log(f"Changing project")
    write_settings(["Settings", "Current_project"], p)
    log(f"Changed project to {p}")
    return

def Header_Agent(info):
    log(f"Modifying custom headers and user-agents to {info["Header"]}, {info["User_agent"]}")
    write_settings(["Projects", Current_project(), "Header"], info["Header"])
    write_settings(["Projects", Current_project(),"User_agent"], info["User_agent"])
    return