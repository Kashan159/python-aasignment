#!/usr/bin/env python
# coding: utf-8

# In[16]:


Islamiat=int(input("Enter marks of the first subject: "))
Urdu=int(input("Enter marks of the second subject: "))
Sindhi=int(input("Enter marks of the third subject: "))
Biology=int(input("Enter marks of the fourth subject: "))
Chemistry=int(input("Enter marks of the fifth subject: "))
sum=Islamiat+Urdu+Sindhi+Biology+Chemistry
print("your number sum is",sum)
per=sum/500*100
print("your persentage is %",per)

if per >= 80 and per <= 100:
    print("your grade is A+")
    
elif per >=70 and per < 80 :
    print("your grade is A")

elif per >=60 and per < 70:
    print("your grade is B")

elif per >=50 and per < 60:
    print("your grade is C")
        
elif per >=40 and per < 50:
    print("your grade is D")
else :
    print("sorry you are fail")


# In[18]:


num = int(input("56: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[3]:


a = [] 
a.append("Hello") 
a.append("hammad") 
a.append("For") 
a.append("python") 
print("The length of list is: ", len(a)) 


# In[4]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[5]:


list1 = [21, 55, 99, 456, 31]
list1.sort()
print("Largest element is:", list1[-1])


# In[17]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:

    if i < 5:

        print(i)


# In[ ]:




