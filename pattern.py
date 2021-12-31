n = int(input("Enter the length: "))
for i in range(n):
    for j in range(n):
        if j<i:
            print("*  ", end = "")
        else:
            print(".  ", end = "")
    print("\n")
for i in range(n):
    for j in range(n):
        if j>=i:
            print("*  ", end = "")
        else:
            print(".  ", end = "")
    print("\n")
