test - e ssshtest || wget - q https: // raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_all_args python3 print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3
assert_stdout
assert_no_stderr    
assert_exit_code 0

run test_missing_args python3 print_fires.py --file_name Agro_short.csv --country Afghanistan
assert_stderr
assert_no_stdout
assert_exit_code 2

run test_afghan_output python3 plot_his.py A_Fires.txt Afghanistan Afghanistan.png Afghanistan_Fires Frequency
assert_equal $file_name $( ls $Afghanistan.png )
assert_no_stderr
assert_exit_code 0

run test_serbia_output python3 plot_his.py S_Fires.txt Serbia Serbia.png Serbia_Fires Frequency
assert_equal $file_name $( ls $Serbia.png )
assert_no_stderr
assert_exit_code 0

run test_croatia_output python3 plot_his.py C_Fires.txt Croatia Croatia.png Croatia_Fires Frequency
assert_equal $file_name $( ls $Croatia.png )
assert_no_stderr
assert_exit_code 0

