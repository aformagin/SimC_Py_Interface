import subprocess
def run_sim(ARGS):
    print("Executing SimCraft")
    COMMAND = '/root/simc'
    simc = subprocess.run([f'{COMMAND}', f'{ARGS}'], check=True, capture_output=True)