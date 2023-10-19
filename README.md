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

Version 4.0

Included continuous integration suite for unit tests, functional tests, and pycodestyle 
at the push and pull request steps.

Version 5.0

I was curious about the frequency of fires that occurred in different countries across all years listed. 
To acquire this, I added a function to the filter_array function in my_utils to output the filtered array as a text file.
From this text file, I am able to generate an output file of fires data seperated by country by using the --out_file flag
when I run print_fires. This text file is then used as the data_file input into the plot_his function. 

plot_his.py takes the following arguments:
data_file: (text file created --output_file flag in print_fires run)
output_file: Name_of_country
title: Name_of_country.png
x: x axis title
y: y axis title

Using plot_his.py, you can plot the frequency of fires over time for any country in the dataset. 
I chose Afghanistan, Serbia, and Croatia. (See accompanied .png files). Overall, Afghanistan
has the lowest frequency of forest fires between all countries. This was an expected result,
as this country has a largely arid climate with mountainous and desert terrain. For most years,
Croatia had between zero and ten fires, with some years extending between 10 and 20 fires/year. 
In one year, Croatia had almost seventy fires, which is likely an outlier in the data. Serbia 
had fewer fires than Croatia overall, with most years displaying between zero and five fires. Serbia
also displays some single-year events in which the frequency fires ranged from 10-20, as well as one year in
which 25 fires occurred. 

This data is isolated, and more context is needed to make meaningful conclusions about these results.
However, a few hypotheses can be made. The first is that the number of fires likely correlates with the
type of landscape present. Serbia and Croatia are much more likely to have forested habitats, and are therefore 
much more likely to experience fires. Other factors, such as annual rainfall, lightning strikes, and human activity
also likely play a roll, though further analysis is needed to verify these claims.    
