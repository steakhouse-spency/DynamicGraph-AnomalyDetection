 
def authors(filename):
    f = open(filename, "r")
    
    # exit if file not in readmode
    if f.mode != 'r':
        exit()
    
    # stream graph text file
    content = f.readlines()
    f.close()

    # iterate through every
    auth = []
    for line in content:
        data = line.split(" ")
        auth.append(data[1].replace("\"", "").replace("_"," ").replace("\n","") )
    return auth

# x = authors("dblp/authorsTop100.txt")
# for i in range(len(x)):
#     print(i, x[i])