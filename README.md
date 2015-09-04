# Description

This repository for Rubicon interview programming exam question#1 - Write a program to process a file:

1. The path to the file is to be passed to the program as a parameter. The file contains zero to more lines. Each line contains zero or more float numbers being separated by one or more space characters.
2. The output of the program is the total count of numbers and the sum of all numbers.
3. List all the ways you plan to test this program.
4. Target to finish this by 30-60 minutes.

# Usage
Below is the usage and a simple running example of this programe:
```
#./bin/floating_number_processing.py -h
SYNOPSIS
    Proccess a text file which contains lines of floating number, print out the number and sum of them.

OPTIONS
    Use the following options to specify a function:
    -h, --help
        Print this usage information
    -f, --file <file path>
        Specify the path of the text file to be processed

EXAMPLES
    # Process file ../tests/normal.txt and print out the result
    ./floating_number_processing.py -f ../tests/normal.txt

#./bin/floating_number_processing.py -f ./tests/normal.txt
Count: 12
Sum: 655.291500
```

# Testing Plan

- Normal Cases:
    - A text file which contains multiple lines, each line with zero or more floating numbers separated by one or more space characters (see ./tests/normal.txt)
    - Remove the line end char '\n' of last line from the file above and test again
- Edge Cases:
    - Empty file
    - The count(int) or sum(float) of floating numbers in the file will cause int or float overflow
    - An extreme large file (the file size is greater than machine memory, e.g. 20GB), which contains multiple lines or even a single long line
- Negative Cases:
    - A text file which contains some invalid floating numbers e.g. 'a4.8' (see ./tests/invalid_float.txt)
    - An arbitrary bianry file
    - The specified file does not exist
