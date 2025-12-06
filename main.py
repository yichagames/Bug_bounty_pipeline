from utils import script_exec
import traceback

command = input("write your command: ").split(" ")
print(command)
try:
    print(script_exec.execute(command))
except Exception as e:
    print(f"From main.py: {e}")
    traceback.print_exc()