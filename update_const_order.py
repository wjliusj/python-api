import argparse
import sys
import utility

File_List = [r'/home/susanl/project/cuTensor/include/cutensor/internal/elementwiseInstancePLC3.h',
             r'/home/susanl/project/cuTensor/include/cutensor/internal/elementwisePrototypePLC3.h',
             r'/home/susanl/project/cuTensor/include/cutensor/internal/operatorsPLC3.h',
             r'/home/susanl/project/cuTensor/include/cutensor/internal/typesPLC3.h',
             r'/home/susanl/project/cuTensor/include/cutensor/internal/utilPLC3.h',
             r'/home/susanl/project/cuTensor/src/consistencyCheckerPLC3.cu',
             r'/home/susanl/project/cuTensor/src/elementwisePLC3.cu',
             r'/home/susanl/project/cuTensor/src/typesPLC3.cpp',
             r'/home/susanl/project/cuTensor/src/utilPLC3.cpp'
            ]


def updateFile(file_name):
    cp_command = "cp -p {} {}.update".format(file_name, file_name)
    utility.command(cp_command)
    f = open(file_name+'.update', 'r+')
    f.truncate()

    context = utility.file_read_lines(file_name)
    for line in context:
        if line.startswith('/*') or line.startswith('*') or line.startswith('//'):
            f.writelines(line)
            continue
        if 'const' in line:
            # split the line with blank part
            word_list = line.split()
            print word_list
            for i in range(len(word_list)):
                if word_list[i] == 'const' or word_list[i].endswith('(const'):
                    # check the next word
                    if (i+1) < len(word_list) and (word_list[i+1].endswith(',') or word_list[i+1].endswith(')')):
                        continue
                    elif (i+2) < len(word_list) and (word_list[i+2].startswith('*') or word_list[i+2].startswith('&') or word_list[i+2][0].isalpha()):
                        # replace order
                        # assume there is only one blank between word_list[i] and word_list[i+1]
                        if word_list[i] == 'const':
                            if word_list[i+1].endswith('*'):
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i+1][:-1]+' '+word_list[i]+'*')
                            elif word_list[i+1].endswith('&'):
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i+1][:-1]+' '+word_list[i]+'&')
                            else:
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i+1]+' '+word_list[i])
                        # endwith '(const'
                        else:
                            if word_list[i+1].endswith('*'):
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i][:-5]+word_list[i+1][:-1]+' '+'const*')
                            elif word_list[i+1].endswith('&'):
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i][:-5]+word_list[i+1][:-1]+' '+'const&')
                            else:
                                line = line.replace(word_list[i]+' '+word_list[i+1], word_list[i][:-5]+word_list[i+1]+' '+'const') 
                            
                        i = i+1
        # write to new file
        f.writelines(line)
        
    rm_command = "rm {}".format(file_name)
    utility.command(rm_command)
    mv_command = "mv {}.update {}".format(file_name, file_name)
    utility.command(mv_command)


def main():
    ret = 0
    
    for file in File_List:
        updateFile(file)
    
    return ret

if __name__ == '__main__':
    sys.exit(main())
