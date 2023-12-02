import subprocess

path = "Path/to/your/compilled/calculator"


def calculator(input_str):
    process = subprocess.Popen(
        path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout.splitlines()
