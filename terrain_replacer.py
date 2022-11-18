

# file directory
file = open("")
newfile = open("tempFileTerrain" , "w")
changeall = False


for i in file:
    if i.__contains__("ocean"):
        print("TRUE")
        x = i.replace("ocean", "plains")
        newfile.write(x)
    else:
        newfile.write(i)

    
