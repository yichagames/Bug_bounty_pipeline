import datetime
import logging
import os

os.makedirs("./logs", exist_ok = True)
os.makedirs("./outputs", exist_ok = True)

logging.basicConfig(filename="./logs/logs.txt", level="DEBUG", format="[%(asctime)s] [%(filename)s] [%(levelname)s] %(message)s")

def log(m, level="info"):
    log_func = getattr(logging, level, logging.info)
    log_func(m)

def output(m):
    with open("./outputs/outputs", "a") as f:
        f.write(f"[{datetime.datetime.now()}]: {m}\n")