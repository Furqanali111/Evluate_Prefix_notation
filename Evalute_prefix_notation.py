#!/usr/bin/env python
# coding: utf-8

# In[1]:


#furqan ali
#200901073
#BS-CS-01-B

from collections import  deque
#creating a class
class prefix_evaluation:
    #creating constructor
    def __init__(self):
        self.equ=[]
    #creating push function
    def push(self,value):
        self.equ.append(value)

    # creating pop function
    def pop(self):
        return self.equ.pop()
    #creation empty function
    def IsEmpty(self):
        return  len(self.equ)==0
    #creating top function
    def top(self):
        return len(self.equ)
    #solving prefix equation
    def Calculating(self, expression):
        for i in reversed(expression):
            if i in '0123456789':
                self.push(i)
            else:
                obj1=self.pop()
                obj2=self.pop()
                result=self.solving_operators(obj1, obj2, i)
                self.push(result)
        return self.pop()
    #performing arithmatic operations
    def solving_operators(self, obj1, obj2, i):
        if i == '/':
            return int(obj1) / int(obj2)
        elif i == '+':
            return int(obj1) + int(obj2)
        elif i == '-':
            return int(obj1) - int(obj2)
        elif i == '*':
            return int(obj1) * int(obj2)
        elif i == '^':
            return int(obj1) ^ int(obj2)

F=prefix_evaluation()
expression=input("Enter prefix expression: ")
value=F.Calculating(expression)

print("Prefix result= ",value)


# In[ ]:




