# Q//
#  Develop a program in Python to
# overload “add” function and
# “equality” operator in a given
# class “LPU”. Display your output
# with proper messages to depict
# how function overloading and
# operator overloading works here.


# class LPU:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         try:
#             return LPU(self.value + other.value)
#         except AttributeError:
#             return LPU(self.value + other)

#     def __eq__(self, other):
#         try:
#             return self.value == other.value
#         except AttributeError:
#             return self.value == other

# value1 = float(input("Enter the first value: "))
# value2 = float(input("Enter the second value: "))

# obj1 = LPU(value1)
# obj2 = LPU(value2)

# result = obj1 + obj2
# print(f"Result of addition: {result.value}")

# if obj1 == obj2:
#     print("Values are equal.")
# else:
#     print("Values are not equal.")


# class lpu:
#     def __init__(self, a):
#         self.a = a

#     def __eq__(self, other):
#         if type(self) == type(other):
#             return self.a == other.a
#         return False
    
#     def sum(self, *args):
#         sum = 0
#         for i in args:
#             sum += i
#         return sum
# a1 = int(input("Enter value for obj1: "))
# a2 = int(input("Enter value for obj2: "))

# obj1 = lpu(a1)
# obj2 = lpu(a2)
# n1 = int(input("Enter value for n1: "))
# n2 = int(input("Enter value for n2: "))
# n3 = int(input("Enter value for n3: "))
# sum_result = obj1.sum(n1,n2,n3)

# print("Sum of n numbers using function overloading is:", sum_result)

# if obj1 == obj2:
#     print("Both the objects contain the same value")
# else:
#     print("Both the objects contain different values")
# set1=set({1,23,34})
# set1.add(16)
# # set1.add(4,4)
# # print(set1)
# print(type(set1))
# set3={}
# print(type(set3))
# dis=dict({1:'akash',2:'pradhan',3:'krish'})
# print("name:%s"%dis[1])
# dis['salaray']=[12,23,45,90000]
# print(dis)
# dis[2]='PradhAn'
# print(dis)
# dis1=dis.update({2:'PRRADHAN'})
# print(dis1)
# print(dis.get(1))
# # print(dis)
# class Akash:
#   def __init__(self,value) :
#      self.value=value
#      print(f"value= {self.value}")
# class b(Akash):
#    def __init__(self, value,sid):
#       self.sid=sid
#       super().__init__(value)
#       print("sid = ",self.sid)

# p1=b(10,20)
# print("value is = ",p1.value)
# print(dir(p1))
# thisdisct={
# "Name":"Akash",
# "Section":"MC123",
# "Class":"MCA"
# }
# x=thisdisct.get("Section")
# print(x)

import pandas as pd
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/dataset_part_2.csv')

data.head()