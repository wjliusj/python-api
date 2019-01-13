#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import json
import os
import shutil
import subprocess
import sys
import utility

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def main():
    ret = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', action='store', default='', help = 'The file need to be checked')
    args = parser.parse_args()
    
    #Process file
    trs_name = os.path.basename(args.file)

    if not os.path.exists(trs_name):
        #cp file to local directory
        cpCmd = "cp -f {} ./".format(args.file)
        ret, output, error = utility.command(cpCmd)
        if ret != 0:
            print("cp file failed with error:"+error)
            sys.exit(1) 
            return ret

    #delete the comments
    sedCmd = "sed -i /'#'/d {}".format(trs_name)
    ret, output, error = utility.command(sedCmd)
    if ret != 0:
        print("sed file failed with error:"+error)
        sys.exit(1) 
        return ret
    #read file context
    fo = open(trs_name, "r")
    filecontext = fo.read()
    print is_json(filecontext)

if __name__ == '__main__':
    sys.exit(main())
