password=input("enter the passward")
encription =password.replace('1','2')\
                      .replace('a','b')\
                      .replace('a','@')
password=encription

print("encripted",password)