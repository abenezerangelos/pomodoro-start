# import sys
#
# array = [1,2,3,4,5]
# array.index(2)
#
# dicter={"play":1,"set":2,"love":3}
# print(dicter.items())
# newarray=array
# i=0
# j=0
# while j<len(array):
#     n=array[i]
#     m=newarray[j]
#     if (n+m)%5==0:
#         print(n,m)
#         break
#     elif i==len(array)-1:
#         j+=1
#     i+=1
# for i in range(7):
#     if i not in array:
#         print(i)
# course="CPT_S"
# def printer(course):
#     print("This is the course %s \n"%course)
# printer(course)
#
# #CPT_s 215 class notes
# def main(*args):
#     for arg in args:
#         print(arg)
# main(1,1,"whatever",[1,1,1,3])
# #c.__class__.name
# #builtin operators that can be overridden _init_(),__repr__ (),__eq__(),__add__()
#
#
#
#
#
#
#
# '''
# We should definitely work on this. Yes, we have to or unless we will not have anything to count on.
# '''
#
#
#
#
#
#
#
#
#
#
# # a possible more relatable implementation of is_prime():time complexity = 0(n^2+n)
# def is_prime2(n):
#
#     for i in range(2,int(number**(1/2))+1):
#         if number%i==0 and is_prime2(i):
#
#             return False
#
#     return True
# #prime generator or prime array
# # we will first try a prime callback function, that will then later on might be applied recursively
# # we will then try the recursive option possibly without generation but actually logic and testing
#
# primal_array=[2]
# def primal(n):
#     for i in primal_array:
#         if n==i:
#             print(True)
#
#             return True
#         for j in range(3,n+1):
#             if j%i!=0:
#                 print(primal_array,1111111)
#                 primal_array.append(j)
#     if n in primal_array:
#         print(True)
#         print(primal_array,22222222)
#         return True
#     else:
#         print(False)
#         print(primal_array, 33333)
#         return False
#
# primal(number)
import sys
import re

m=re.search('[a]','aaaaabcdefjlkjaljalkjaaaaaa')
m=m.group()
print(sys.argv[1],sys.argv[2])
with open(sys.argv[1],'r') as f:
    things=f.readlines()
print(things)
words=''
for item in things:
    words+=item
print(words)


