from string import *
message = input("enter your message: ")
import time
def main():
    letters = 'abcdefhgijklmnopqrstuvxyz'
    val = letters[-1] + letters[0:-1]

    encrypt = dict(zip(letters,val))
    Decrypt = dict(zip(letters,val))

    e_D = input("E / D: ")

    if e_D == "E":
        mssg = ''.join([encrypt[letter]
                            for letter in message()])
    elif e_D == "D":
        mssg = ''.join([Decrypt[letter]
                            for letter in message()])

    else:
        print("invalid Command")

    return mssg
if __name__ == '__main__':
    print(main())
