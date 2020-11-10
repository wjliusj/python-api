import argparse
import sys
import utility

App_Dir = "/home/susanl/p4source/sw/rel/gpgpu/toolkit/r10.2_safe/cuda/apps"

def main():
    ret = 0
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='file', action='store', default='', help='The file needs to be used')
    args = parser.parse_args()
    file = args.file
    file_name = file.split('.')[0]

    # get api name from each line
    lines = utility.file_read_lines(file)
    # print raw log to output_raw.log
    raw_log = 'output_raw_'+file_name+'.log'
    app_log = 'app_'+file_name+'.log'
    f_raw = open(raw_log, 'w')
    # print app to app.log
    f_app = open(app_log, 'w')
    for api in lines:
        api = api.strip()
        grep_cmd1 = "sudo grep -r {0} {1}/*".format(api + '\(', App_Dir)
        grep_cmd2 = "sudo grep -r {0} {1}/*".format(api+'\ ', App_Dir)
        print>>f_raw, grep_cmd1,grep_cmd2
        ret1, output1, error1 = utility.command(grep_cmd1, False)
        ret2, output2, error2 = utility.command(grep_cmd2, False)
        if ret1 != 0 and ret2 != 0:
            print("Error: cmd {} failed with error: {}".format(grep_cmd1, error1))
            print("Error: cmd {} failed with error: {}".format(grep_cmd2, error2))
        print>>f_raw, output1+output2

        # find app from the output
        output_list = (output1+output2).split('\n')
        specail_case = True
        for item in output_list:
            if 'parms.res[i]' in item:
                full_path_file = item.split(':')[0]
                app = full_path_file.split('/')[-2]
                print(app)
                print >> f_app, app
                specail_case = False
        if specail_case:
            print("Special case {}!!! Need to check in the raw log!".format(api))
            print >> f_app, "Special case {}!!! Need to check in the raw log!".format(api)
        

if __name__ == '__main__':
    sys.exit(main())
