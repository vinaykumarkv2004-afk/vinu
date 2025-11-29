article=["a","an"]
sentance=input("enter the sentance to remove article:")
result=sentance
for i in article:
 result=result.replace(i,'')
result=result.replace(i.capitalize(),'')
result=' '.join(result.split())
print(result)