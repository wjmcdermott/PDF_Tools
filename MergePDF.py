#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
from argparse import ArgumentParser
from glob import glob
from pyPdf import PdfFileReader, PdfFileWriter

DIR_NAME = 'M:\\Movies\\Science'
EXTENSION = ".zip"

def merge(path, output_filename):
    """ Merge path and filename """
    output = PdfFileWriter()

    for pdffile in glob(path + os.sep + '*.pdf'):
        if pdffile == output_filename:
            continue
        print("Parse '%s'" % pdffile)
        document = PdfFileReader(open(pdffile, 'rb'))
        for i in range(document.getNumPages()):
            output.addPage(document.getPage(i))

    print("Start writing '%s'" % output_filename)
    with open(output_filename, "wb") as f:
        output.write(f)

if __name__ == "__main__":
    PARSER = ArgumentParser()

    # Add more options if you like
    PARSER.add_argument("-o", "--output",
                        dest="output_filename",
                        default="merged.pdf",
                        help="write merged PDF to FILE",
                        metavar="FILE")
    PARSER.add_argument("-p", "--path",
                        dest="path",
                        default=".",
                        help="path of source PDF files")


def dir_unzip():
    """ Unzip all files in path """
    os.chdir(dir_name) # change directory from working dir to dir with files
    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file
