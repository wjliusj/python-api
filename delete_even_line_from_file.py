#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import sys
import utility

def main():
    ret = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', action='store', default='', help = 'The file needs to be processed')
    args = parser.parse_args()
    
    #delete the comments
    sedCmd = "sed -i '0~2d' {}".format(args.file)
    ret, output, error = utility.command(sedCmd)
    if ret != 0:
        print("sed file failed with error:"+error)
        sys.exit(1) 
        return ret

if __name__ == '__main__':
    sys.exit(main())
