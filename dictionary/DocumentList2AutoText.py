#!/usr/bin/python3
########################################################################
# Name: Script DocumentList2AutoText.py
# Author: J. Papasian
#
# Description: Download latest DocumentList from LibreOffice source
# and converts it for usage in AnySoftKeyboard
#
# Usages:
# ./DocumentList2AutoText fr > autotext_fr.xml
# ./DocumentList2AutoText en > autotext_en.xml
#
# Prerequisite: python3
# Script license: Beerware
# LibreOffice license: LGPLv3+
########################################################################

import xml.etree.ElementTree as ET
import urllib.request,sys
from xml.sax.saxutils import escape,quoteattr

def execute(lang):
    url = 'https://cgit.freedesktop.org/libreoffice/core/plain/extras/source/autocorr/lang/'+lang+'/DocumentList.xml'
    source = urllib.request.urlopen(url)
    root = ET.fromstring(source.read())

    print('<?xml version="1.0" encoding="utf-8"?>')
    print('<words>')
    for child in root:
        fromvalue = child.get('{http://openoffice.org/2001/block-list}abbreviated-name')
        tovalue = child.get('{http://openoffice.org/2001/block-list}name')
        print('<word src='+quoteattr(fromvalue)+'>'+escape(tovalue)+'</word>')
    print('</words>')

execute(sys.argv[1]);
