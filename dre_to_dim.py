import sys

class DreToDim(object):

    def process(self, inFile, outFile):
        outData = []
        
        # Read data
        data = self.read_from_file_simple(inFile)
        
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
        offset = 0
        data.pop(len(data) - 1)

        for i, line in enumerate(data):
            lineArray = line.split(" ")
            node = int(lineArray.pop(0)[:-1])

            if(node == 0):
                offset = 1
            
            node += offset
            lines = []

            for j, destNodeStr in enumerate(lineArray):
                destNode = int(destNodeStr.replace('.', '')) + offset
                newLine = "e "+ str(node) + " " + str(destNode)

                if(i == len(data)):
                    continue

                outData.append(newLine)
        
        self.write_to_file_simple(outFile, outData)

    def read_from_file_simple(self, path):
        """
        Read line by line from a file
        :param path: 
        :return: 
        """
        with open(path) as f:
            data = f.readlines()
        data = [x.strip() for x in data]
        return data

    def write_to_file_simple(self, path, data):
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
        print("Error. \n Incorrect number of arguments. \n Usage 'python dre_to_dim.py {drefile}.dre {dimacsfile}'. \n")
        exit()

    # Init
    x = DreToDim()
    x.process(sys.argv[1], sys.argv[2])
