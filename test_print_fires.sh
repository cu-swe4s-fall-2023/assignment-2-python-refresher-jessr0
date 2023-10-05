test - e ssshtest | | wget - q https: // raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_all_args python print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3
assert_stdout
assert_no_stderr    
assert_exit_code 0

run test_missing_args python print_fires.py --file_name Agro_short.csv --country Afghanistan
assert_stderr
assert_no_stdout
assert_exit_code 2

run test_mean_output python print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3 --stat_op mean
assert_in_stdout 0.0
assert_no_stderr
assert_exit_code 0

run test_median_output python print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3 --stat_op median
assert_in_stdout 0.0
assert_no_stderr
assert_exit_code 0

run test_statdev_output python print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3 --stat_op 'standard deviation'
assert_in_stdout 0.0
assert_no_stderr
assert_exit_code 0

run test_badstat_output python print_fires.py --file_name Agro_short.csv --country Afghanistan --country_column 0 --fires_column 3 --stat_op smean
assert_in_stdout[0, 0, 0, 0]
assert_no_stderr
assert_exit_code 0
