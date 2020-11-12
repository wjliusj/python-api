# Input:
# 1. excel which stores the test results
# 2. txt which stores the required tests
# Output:
# 1. excel which only stores the test results for the required tests


import xlwt
import xlrd
import utility

# the item should be "acos:(PASSED, 10)"
required_tests_infor_map = {}
tests_infor_map = {}

# get the required tests from the input txt
input_txt = r"C:\0work\orin\QNX_test_results\temp\L1-testlist.part4_remain_filter_cnp"
required_tests = utility.file_read_lines(input_txt)
print(type(required_tests))
print(len(required_tests))
print(required_tests[0])

# get the test results from the input excel
input_excel = r"C:\0work\orin\QNX_test_results\temp\L1_L4T_results.xls"
input_data = xlrd.open_workbook(input_excel)
input_sheet = input_data.sheet_by_index(0)
col_test_values = input_sheet.col_values(0)
col_result_values = input_sheet.col_values(5)
col_time_values = input_sheet.col_values(6)

for i in range(2, len(col_test_values)):
    test = col_test_values[i]
    test_infor = (col_result_values[i], col_time_values[i])
    tests_infor_map[test] = test_infor

print(type(tests_infor_map))
print(len(tests_infor_map))
print(tests_infor_map[col_test_values[2]])
print(tests_infor_map[col_test_values[len(col_test_values)-1]])

# create a new sheet as output
print(required_tests)
required_tests_infor_map = {required_test.strip(): tests_infor_map[required_test.strip()] for required_test in required_tests}
print(len(required_tests_infor_map))

output_excel = r"C:\0work\orin\QNX_test_results\temp\L1_required_results.xls"
output_data = xlwt.Workbook()
output_sheet = output_data.add_sheet("output")
for i in range(len(required_tests)):
    test = required_tests[i].strip()
    output_sheet.write(i, 0, test)
    output_sheet.write(i, 1, required_tests_infor_map[test][0])
    output_sheet.write(i, 2, required_tests_infor_map[test][1])

output_data.save(output_excel)



