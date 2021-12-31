# for the binary value
# number = ''
# def hexadecimal():
#     if length != n:
#         for digit in digits:
#             number +=digit
#             length +=1
#             print(number)
# n = int(input("Enter the length: "))

# if length != n:
#     hexadecimal()

def hexadecimal(n): # n --> for what value
    digits = ['1', '2', '3', '4',  '5', '6','7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    length = ''
    pos = 0
    for i in range(1, 100):
        for digit in digits:
            if pos == n:
                break
            else:
                pos+=1
                length =length + digit
                print(length)
                length =length[0: len(length)-1]
        length = str(i)
def octal(n):
    for i in range(1, n+1):
            if str(i)[-1]=='8' or str(i)[-1]=='9' or str(i)[-1]=='0':
                i = i+2
            print(i)

def decimal(n):
    for i in range(1, n+1):
        print(i)
n = int(input('Enter the length: '))
print(f'{decimal(n)} {octal(n)} {hexadecimal(n)}')