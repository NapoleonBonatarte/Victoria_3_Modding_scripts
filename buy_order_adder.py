

# file directory
file = open("")

newfile = open("tempFileBuyPackages" , "w")
changeall = False



x = 1
for i in file:
    newfile.write(i)
    if i.__contains__("\tgoods = "):
        newfile.write("\t\tpopneed_space_survival_gear = " + str(x) + "\n")
        x += 1
