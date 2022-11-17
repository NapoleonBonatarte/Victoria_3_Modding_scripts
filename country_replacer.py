
#file = open(input("enter file"))
file = open("C:/Code/Personal code/victoria_3_scripts/00_states.txt")
newfile = open("tempFile" , "w")

for i in file:
    if i.__contains__("\t\t\tcountry = "):
        newfile.write("\t\t\tcountry = c:USC\n")
        print("TRUE")
    else:
        newfile.write(i)