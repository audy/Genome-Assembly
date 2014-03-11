'''

    This script provides a way to split a fasta file into to two subfiles

    Usage: python split_fasta.py <input file> <splitting argument>

    Author: Nicolas Schmelling

'''

import sys

def split(in_file, split):
    new = open('1.fasta','w')
    with open(in_file,'r') as tf:
        count = 0
        for line in tf:
            if line.startswith('>'):
                count += 1
            if count == split:
                new.close()
                count = 0
                new = open('2.fasta', 'w')
            new.write(line)
    new.close()

if __name__ == "__main__":
    in_file = sys.argv[1]
    split = int(sys.argv[2])
    
    split(in_file, split)
