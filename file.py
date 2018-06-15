import os
import fileinput
import json
import re

def filter(intxt, outtxt, oldfile, newfile):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r', encoding='utf-8') as infile:
        for line in infile:
            if intxt in line:
                line = outtxt
            outfile.write(line)

def filter2(intxt, outtxt, oldfile):
    with fileinput.input(inplace=True, files=(oldfile), backup='.bkp') as infile:
        for line in infile:
            #line = line.replace(intxt, outtxt)
            line = 
            print(line, end='')



#with open('data.json') as f:
#    data = json.load(f)
#    intext = data["string1"]["stringinput"]
#    outtext = data["string1"]["stringoutput"]
#    inputfile = data["file"]["inputfile"]

#with open('data2.json') as f1:
#    data2 = json.load(f1)
#    for key in data2:
#        inputfile = 
#        intext = data[key]
#        outtext = data2[value]

with open('data3.json') as f:
    data = json.load(f)
    for i in data['file']:
        intext = i["stringinput"]
        outtext = i["stringoutput"]
        inputfile = i["inputfile"]
        print(intext)
        print(outtext)
        print(inputfile)
        letsgo4 = filter2(intext, outtext,inputfile)

        #print("The key and value are ({}) = ({})".format(key, value))

# intext = input('Please enter the name of a great person: ')    
# outtext = input('Please enter the name of a great person: ')    

# letsgo = filter(intext, outtext,'input.txt', 'output.txt')
# letsgo2 = filter2(intext, outtext,'input.txt')
# letsgo3 = filter2(intext, outtext,inputfile)
letsgo4 = filter2(intext, outtext,inputfile)
