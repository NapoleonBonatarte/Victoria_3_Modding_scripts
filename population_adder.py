

file = open("C:/Code/Personal code/victoria_3_scripts/datafolder/05_north_america.txt")
newfile = open("tempFilePopulation" , "w")
changeall = False



for i in file:
    if i.__contains__("\t\tregion_state:"):
        newfile.write("\t\tregion_state:USC = {\n")
    else:
        newfile.write(i)