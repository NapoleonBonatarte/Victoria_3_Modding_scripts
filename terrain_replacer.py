


file = open("C:/Code/Personal code/victoria_3_scripts/province_terrains.txt")
newfile = open("tempFileTerrain" , "w")
changeall = False


for i in file:
    if i.__contains__("ocean"):
        print("TRUE")
        x = i.replace("ocean", "plains")
        newfile.write(x)
    else:
        newfile.write(i)

    