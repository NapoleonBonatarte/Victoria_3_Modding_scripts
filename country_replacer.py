
#file = open(input("enter file"))
file = open("C:/Code/Personal code/victoria_3_scripts/datafolder/00_states.txt")
newfile = open("tempFile" , "w")
changeall = False


for i in file:
    if changeall:
        if i.__contains__("\t\t\tcountry = ") and not i.__contains__("\t\t\tcountry = c:USC"):
            newfile.write("\t\t\tcountry = c:USC\n")
            print("TRUE")
        else:
            newfile.write(i)
    else:
        if i.__contains__("\t\t\tcountry = "):
            newfile.write("\t\t\tcountry = c:IRC\n")
            print("TRUE")
        else:
            newfile.write(i)