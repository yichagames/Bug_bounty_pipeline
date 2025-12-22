import subprocess as run
from utils.log import log

def execute(c):
    try:
        log(f"Now running: {' '.join(c)}")
        return run.check_output(c, text=True)
    except run.CalledProcessError as e:
        log(f"subprocess {' '.join(c)} failed unexpectedly: {e}")
        return f"subprocess {' '.join(c)} failed unexpectedly: {e}"