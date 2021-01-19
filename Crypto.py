from string import *
message = input("enter your Keys: ")
import time
def main():
    Keys = 'abcdefhgijklmnopqrstuvwxyz !1234567890()*&^%$#@={}[]:.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    value = Keys[-1] + Keys[0:-1]

    encrypt = dict(zip(Keys,value))
    Decrypt = dict(zip(value,Keys))

    e_D = input("E / D: ")

    if e_D == "E":
        NewMessage = ''.join([encrypt[letter]
                            for letter in message])
    elif e_D== "D":
        NewMessage = ''.join([Decrypt[letter]
                            for letter in message])

    else:
        print("invalid Command")

    return NewMessage

print(main())
