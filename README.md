[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# python-refresher

Version 1.0
Generated a get_column function to source fires from the Agrofood csv file. 
The function allows the user to sort fires by country (or in theory any other parameter), 
and outputs an array that contains fires associated with that value. Parameters are defined
in the print_fires script. The function has two steps. 
The first step takes the file and sorts each line into its own array, 
and compiles those into a larger array called array_con. 
The second portion iterates through each array by the user-defined 
query value and outputs the values in the corresponding results column, 
printed as a new array. 
The first iteration of thisdemanded that the user define the desired results column, 
the second iteration sets the results column to 1 automatically.

Version 2.0
Created a set of arguments that require the user to define file name, country,
country column, and fires column as part of the run parameters.

Fundamental functions are the same as the previous version. 

The first step sorts each line in the designated file into its own array, 
and compiles them into a large array. 

The second step iterates through each array and outputs the value in the fires
column that corresponds to the country of interest. 

The third step takes this array and converts it into a list of integers. 

Exceptions are included for errors in file loading and opening, as well as
value errors when converting the array to integers. All will generate error codes
and descriptions.

my.utils contains the code that performs the aforementioned three step process.
print.fires contains the arguments and the main function that imports and runs the
utility script. run.sh runs print.fires.

Version 3.0

print.fires now accepts arguments for one of three optional statistical operations 
(mean, median, or standard deviation). Choosing not to perform statistics will return the
list of integers.

Syntax of print fires in run.sh: python print_fires.py --arg "" --arg "" ...
To run print_fires.py: bash run.sh

Unit and functional tests are now included

Running unit tests:
python test_my_utils.py

Running functional tests:
bash test_print_fires.sh   
