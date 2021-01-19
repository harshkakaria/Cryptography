def main():
    letters = 'abcdefhgijklmnopqrstuvxyz'
    val = keys[-1] + keys[0:-1]

    encrypt = dict(zip(letters,val))
    Decrypt = dict(zip(letters,val))

    message = input("enter your message: ")
    e_D = input("E / D: ")
    if e_D == "E":
        
