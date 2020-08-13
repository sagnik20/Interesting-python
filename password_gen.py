import random,string
def password(l):
    pass_char = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(pass_char) for i in range(l))
    print("Your Password is: ", passw)
password(int(input("Enter the length of password you want: ")))