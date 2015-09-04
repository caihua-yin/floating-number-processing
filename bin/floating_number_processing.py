#!/usr/bin/python

"""
This program process a text file which contains zero to more lines. 
Each line contains zero or more float numbers being separated by one or more space characters.

The output of the program is the total count of numbers and the sum of all numbers.
"""

import getopt
import sys
import os

def usage():
    """
    Print usage
    """
    usage_str = """
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
    ./%s -f ../tests/normal.txt
    """
    print usage_str % (os.path.basename(sys.argv[0]),)

def getopts():
    """
    Get command opt arguments
    """
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hf:", ["help", "file="])
        return opts
    except getopt.GetoptError:
        usage()

def process_file(file_path):
    """
    Process the input file and print out the count and sum of floating numbers in it
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print "The input file %s does not exist." % file_path
        sys.exit(1)

    count = 0
    summation = 0.0
    with open(file_path) as fp:
        # Read file chunk by chunk in ~4K size,
        # process each chunk, and aggregate the result of them
        for chunk in read_file_in_chunk(fp):
            c, s = process_chunk(chunk)
            count += c
            summation += s
    print "Count: %d" % count
    print "Sum: %f" % summation

def read_file_in_chunk(file_object, hint_size=1024*4):
    """
    Read file in chunks with specified hint size, default as 4K
    On hint size reached, the chunk will end with empty space between two float numbers or '\n' between lines

    This is to handle some extreme large file or long line scenario.
    """
    while True:
        data = file_object.read(hint_size)

        # Reach to the end of the file
        if not data:
            break

        # The read data does not end with a float number.
        # Need read further characters until reaching ' ', '\n' or the end of the file
        if data[-1] != ' ' or data[-1] != '\n':
            while True:
                char = file_object.read(1)
                if char == ' ' or char == '\n' or not char:
                    break
                else:
                    data += char                    
        yield data

def process_chunk(chunk):
    """
    Process the string chunk which contains zero or more float numbers being separated by one or more space characters

    Returns:
    The tuple of (count, summation) of the floating numbers
    """
    count = 0
    summation = 0.0
    for float_str in chunk.split():
        try:
            float_num = float(float_str)
            count += 1
            summation += float_num
        except ValueError:
            print "Invalid floating number encountered: %s" % float_str
            sys.exit(1)

    return (count, summation)

def main():
    """
    The main function
    """
    # Set default command option value
    cmd = None
    file_path = None

    # Get command option and call corresponding function
    opts = getopts()
    for option, value in opts:
        if option in ("-h", "--help"):
            cmd = "help"
        elif option in ("-f", "--file"):
            cmd = "process"
            file_path = value
        else:
            usage()
            sys.exit(1)

    if cmd == "help":
        usage()
    elif cmd == "process":
       process_file(file_path)
    else:
        usage()
        sys.exit(1)

if __name__ == '__main__':
    main()
