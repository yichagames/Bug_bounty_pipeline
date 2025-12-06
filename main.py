import subprocess as run

try: 
    ans = run.check_output(["ls"], text=True)
    print(ans)
except run.CalledProcessError as e:
    print(f"Command failed with return co")