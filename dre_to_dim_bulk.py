import sys
from dre_to_dim import DreToDim

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Error. \n Incorrect number of arguments. \n Usage 'python dre_to_drim_bulk.py {dreFolder} {dimacsFolder}'. \n")
        exit()

    # Init
    inFolder = sys.argv[1]
    outFolder = sys.argv[2]

    x = DreToDim()
