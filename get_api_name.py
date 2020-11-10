import argparse
import sys
import utility

def main():
    ret = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', action='store', default='', help='The file needs to be processed')
    args = parser.parse_args()

    file = args.file
    # delete the even line
    sedCmd = "sed -i '0~2d' {}".format(file)
    ret, output, error = utility.command(sedCmd)
    if ret != 0:
        print("sed file failed with error:" + error)
        sys.exit(1)
        return ret

    # get api name from each line
    lines = utility.file_read_lines(file)
    for line in lines:
        word_list = line.split(' ')
        temp_index = word_list.index('(')
        current_api = word_list[temp_index-1]
        print(current_api.strip())


if __name__ == '__main__':
    sys.exit(main())