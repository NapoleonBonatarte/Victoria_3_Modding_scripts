
#file = open(input("enter file"))
# file directory
file = open("")
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
