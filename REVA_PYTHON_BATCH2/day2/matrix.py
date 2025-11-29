list_of_tuple=eval(input("enter the list of tuples"))
k=int(input("enter the column indx"))
product=1
for i in list_of_tuple:
    if k<len(i):
        product=product*i[k]
    else:
        print(f"invalid(k)")
        break
print(product)
     

