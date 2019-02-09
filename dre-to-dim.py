import sys

def read_from_file_simple(path):
    """
    Read line by line from a file
    :param path: 
    :return: 
    """
    with open(path) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    return data

def write_to_file_simple(path, data):
    """
    Write to file using raw strings
    - Print line by line using new line separators
    :param path: 
    :param data: 
    :return: 
    """
    with open(path, 'w') as outfile:
        for datum in data:
            out = datum
            if datum != data[-1]:
                out = out + "\n"
            outfile.write(out)


if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print "Error. \n Incorrect number of arguments. \n Usage 'python {drefile}.dre {dimacsfile}'. \n"
        exit()

    # Init
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    outData = []
    
    # Read data
    data = read_from_file_simple(inFile)
    
    # Process input data
    header = data.pop(0)
    header_array = header.split(" ")
    
    # Nodes
    for i, v in enumerate(header_array):
        if("n" not in v):
            continue
        
        nodes = v[2:]

    # Edges
    edges = 0
    for i, v in enumerate(data):
        edges += len(v.split(" ")) - 1


    # Process output data
    outHeader = "p edge "+ str(nodes) + " " + str(edges)
    outData.append(outHeader)

    # Rows
    for i, v in enumerate(data):
        line = v.split(" ")
        node = line.pop(0)[:-1]
        lines = []

        for j, v2 in enumerate(line):
            newLine = "e "+ str(node) + " " + str(v2)
            newLine = newLine.replace('.', '')

            if(i == len(data) - 1):
                continue

            outData.append(newLine)
    
    write_to_file_simple(outFile, outData)
