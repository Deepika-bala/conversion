decimal=int(input("enter the decimal : "))
convert =int(input("convert into : [1] binary,[2] octal,[3] hexadecimal:\n"))
if convert == 1:
    print("convert into binary\n " ,bin(decimal))
elif convert == 2 :
    print("convert into octal\n", oct(decimal))
elif convert == 3:
    print("convert into octadecimal\n",hex(decimal))
else:
    print("check the input")

