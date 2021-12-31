def print_formatted(number):
    # your code goes here
    for i in range(1, n+1): #decimal value
        print(i)
    for i in range(1, n+1):  # octal value
        if str(i)[-1]=='8' or str(i)[-1]=='9' or str(i)[-1]=='0':
            i = i+2
        print(i)

    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)