
Input=raw_input("Enter Your Name\n")

if Input in open('input.txt').read():
    print("name already in file")
else:
    with open("input.txt", "a") as myfile:
        myfile.write(Input)
    print ("Success name added to file")