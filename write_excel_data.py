# Input:
# 1. txt which stores the test results
# 2. excel stores the tests with certain order
# Output:
# 1. update excel with the tests' status


import xlrd
import xlwt
import openpyxl
import utility


tests_infor_map = {}

# ###############################################################################################  #
# Find the line starts with "Test line is :", the test name is after "Test line is :".             #
# The test status should be the last non-empty line before next line starts with "Test line is :"  #
# For the last test, its test status should be the last non-empty line in the txt                  #
####################################################################################################

input_txt = r"C:\0work\orin\QNX_test_results\temp_for_write_excel_data\L1_test_results.txt"
lines = utility.file_read_lines(input_txt)
lines = utility.remove_blanks_characters(lines)

current_test = None
for i in range(len(lines)):
    line = lines[i]
    previous_test = current_test
    if line.startswith("Test line is :"):
        current_index = i
        current_test = line.split("Test line is :", 1)[1]
        if current_index!=0:
            # The status of the previous test should be just above current test
            tests_infor_map[previous_test] = lines[current_index-1]

# Add the last test infor to the map
print(current_test)
tests_infor_map[current_test] = lines[len(lines)-1]

print(tests_infor_map)


# ###############################################################################################  #
# Write the results to the excel with original tests order                                         #
# The test name are saved at column A, need to input the test status to column B                   #
####################################################################################################
input_excel = r"C:\0work\orin\QNX_test_results\temp_for_write_excel_data\L1_test_results.xlsx"
# input_data = xlrd.open_workbook(input_excel)
# input_sheet = input_data.sheet_by_index(0)
# col_test_values = input_sheet.col_values(0)
wb = openpyxl.load_workbook(input_excel)
my_sheet = wb.worksheets[0]
test_column = my_sheet['A']

get_result_num = 0
for i in range(len(test_column)):
    test = test_column[i].value
    if test in tests_infor_map.keys():
        test_status = tests_infor_map[test]
        my_sheet["B"+str(i+1)] = test_status
        get_result_num = get_result_num + 1

wb.save(input_excel)


print("get_result_num is: ", get_result_num)
