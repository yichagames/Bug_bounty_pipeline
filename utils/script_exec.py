import subprocess as run
from utils import log

def execute(c):
    try:
        log.log(f"Now running: {' '.join(c)}")
        return run.check_output(c, text=True)
    except run.CalledProcessError as e:
        return "looks like ts func is kinda unc tho idk prob cuz: " + e