import sys
import os
from dre_to_dim import DreToDim


def load_files(inFolder):
    files = []
    for fileName in run_command('ls -v ' + inFolder):
        files.append(fileName)
    return files


def run_command(command):
    """
    Run a command and return a list
    Good for single lined commands
    :param command: 
    :return: 
    """
    p = os.popen(command, "r")
    out = []
    while 1:
        line = p.readline()
        if not line:
            break
        out.append(line.rstrip())
    return out


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print ("Error. \n Incorrect number of arguments. \n Usage 'python dre_to_drim_bulk.py {dreFolder} {dimacsFolder}'. \n")
        exit()

    # Init
    inFolder = sys.argv[1]
    outFolder = sys.argv[2]

    x = DreToDim()
    files = load_files(inFolder)
    for i, fileName in enumerate(files):
        inFileName = inFolder + "/" + fileName
        outFileName = outFolder + "/" + fileName.replace('.dre', '')
        x.process(inFileName, outFileName)

