

# file directory
file = open("")
newfile = open("tempFilePopulation" , "w")
changeall = False



for i in file:
    if i.__contains__("\t\tregion_state:"):
        newfile.write("\t\tregion_state:USC = {\n")
    else:
        newfile.write(i)
