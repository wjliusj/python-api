import os
import subprocess

def command(cmd, is_output = True):
    #Need shell=True since exe parameter possibly be a string with arguments
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (output, error) = p.communicate()
    if output and is_output:
        print(output),
    if error and is_output:
        print(error),
    return p.returncode, output, error


# Read all context,
# If the file exists, return its context as list
# Else, return -1
def file_read_lines(file):
    if os.path.exists(file):
        f_file = open(file, "r")
        lines = f_file.readlines()
        f_file.close()
        return lines
    else:
        raise ValueError("The file {} is not exist!!!".format(file))