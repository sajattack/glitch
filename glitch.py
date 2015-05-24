#! /usr/bin/env python
docstring = '''Randomly changes binary file data in order to create glitch art.
    Usage: glitch <infile> [percentage] [outfile]
        infile: the file to take as input
        percent: the percentage of the file to corrupt, by default, 0.1%
        outfile: the file to output, by default <filename>-glitched.<fileext>
    '''

import sys, os, random

headersize = {'jpg': 9, 'png': 8, 'bmp': 54, 'gif': 14, 'tiff': 8}  

def glitch(infile, percent, outfile):
    with open(infile, 'rb') as inf:
        with open(outfile, 'wb') as outf:

            #copy file header
            fileext = infile.split(".")[1]
            try:
                for byte in range(headersize[fileext]):
                    inbyte = inf.read(1)
                    outbyte = inbyte
                    outf.write(outbyte)
            except KeyError:
                pass
                
            while True:
                inbyte = inf.read(1)
                if not inbyte:
                    break
                if (random.random() < percent/100):
                    outbyte = os.urandom(1)
                    #outbyte = '\x00' 
                else:
                    outbyte = inbyte
                outf.write(outbyte)


if __name__ == "__main__":
    argc = len(sys.argv)
    if (argc == 2):
        infile = sys.argv[1]
        percent = 0.1
        filename = infile.split(".")[0]
        fileext = infile.split(".")[1]
        outfile = filename + "-glitched" + "." + fileext
        glitch(infile, percent, outfile)
    elif (argc == 3):
        infile = sys.argv[1]
        percent = float(sys.argv[2])
        filename = infile.split(".")[0]
        fileext = infile.split(".")[1]
        outfile = filename + "-glitched" + "." + fileext
        glitch(infile, percent, outfile)
    elif (argc == 4):
        infile = sys.argv[1]
        percent = float(sys.argv[2])
        outfile = sys.argv[3]
        glitch(infile, percent, outfile)
    else:
       print(docstring)
        
