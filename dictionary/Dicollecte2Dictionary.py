#!/usr/bin/python3
########################################################################
# Name: Script Dicollecte2Dictionary.py
# Author: J. Papasian
#
# Description: Convert a Dicollecte Lexique to
# xml for usage in AnySoftKeyboard
#
# Usages:
# ./Dicollecte2Dictionary.py lexique-dicollecte-fr-v6.0.2.txt > words_fr_dicollecte.xml
#
# Prerequisite: python3
# Script license: Beerware
# Dicollecte license: MPL
########################################################################

import sys,csv
from xml.sax.saxutils import escape,quoteattr

def execute(inputfile):
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print('<wordlist>')
    with open(inputfile, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in csvreader:
            if len(row) > 17 and row[0] != 'id' and float(row[17])*100000000 > 1:
                print('<w f='+quoteattr(str(int(float(row[17])*100000000)))+'>'+escape(row[1])+'</w>')
    print('</wordlist>')

execute(sys.argv[1]);
