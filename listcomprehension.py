# 1-10 even numbers

for i in range(1,11):
    if i%2==0:
        print(i)


#list comprehension
l=[i for i in range(1,11) if i%2==0]
print(l)


l=[]
s="Hello world"
for i in s:
    l.append(i)
print(l)


#list comprehension
l1=[x for x in "Hello World"]
print(l1)


l2=[i for i in "Hello Everyone how are you all " if i==" " ]
print(len(l2))

l=[i for i in range(1,101) if "6" in str(i) ]
print(l)


"""
    nested loops in list comprehension
"""

# for i in range(1,5):
#     for j in range(1,4):
#         print(i,j)

l=[[j for j in range(1,4)] for i in range(1,5)]
print(l)

l=[i*10 for i in range(1,5)]
print(l)




# if - else
for i in range(1,6):
    if i%2==0:
        print("it is even")
    else:
        print("it is odd")


l=["it is even" if i%2==0 else "it is odd" for i in range(1,6)]
print(l)