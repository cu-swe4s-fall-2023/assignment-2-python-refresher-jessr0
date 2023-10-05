#!/bin/bash

python print_fires.py --file_name "Agro_short.csv" --country "Afghanistan" --country_column 0 --fires_column 3 --stat_op median

set +e
python print_fires.py --file_name "Agrofood_co2_emission.csv" --country "United States of America" --country_column 0 --fires_column 0 

python print_fires.py --file_name "Agrufood_co2_emission.csv" --country "United States of America" --country_column 0 --fires_column 3
set -e
