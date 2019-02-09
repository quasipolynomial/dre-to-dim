import sys

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print "Error. \n Incorrect number of arguments. \n Usage 'python {drefile}.dre {dimacsfile}'. \n"
        exit()
        
    #print("\n".join(sys.argv))
    print(sys.argv[1])