

file = open("C:/Code/Personal code/victoria_3_scripts/00_buy_packages.txt")
newfile = open("tempFileBuyPackages" , "w")
changeall = False



x = 1
for i in file:
    newfile.write(i)
    if i.__contains__("\tgoods = "):
        newfile.write("\t\tpopneed_space_survival_gear = " + str(x) + "\n")
        x += 1