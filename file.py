import os
import fileinput
import json
import re

def filter(intxt, outtxt, oldfile):
    with fileinput.input(inplace=True, files=(oldfile), backup='.bkp') as infile:
        for line in infile:
            line = line.replace(intxt, outtxt)
            print(line, end='')

with open('data3.json') as f:
    data = json.load(f)
    for i in data['file']:
        intext = i["stringinput"]
        outtext = i["stringoutput"]
        inputfile = i["inputfile"]
        print(intext,outtext)
        runme = filter(intext, outtext,inputfile)

