
# store graph in adjacency matrix
    #scipi
    

# file streaming
file = "testData.txt"
print("yeet: ", file)

f = open(file, "r")


if f.mode == 'r':
    content = f.readlines()
    print("contents\n",content)
    i = 0
    for line in content:
        data = line.split(" ")
        n1 = int(data[0])
        n2 = int(data[1])
        w = int(data[2])
        
        i+=1
    
else:
    exit()



    