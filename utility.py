import subprocess

def command(cmd):
    #Need shell=True since exe parameter possibly be a string with arguments
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (output, error) = p.communicate()
    if output:
        print(output),
    if error:
        print(error),
    return p.returncode, output, error

