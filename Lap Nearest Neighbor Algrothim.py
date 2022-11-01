# -*- coding: utf-8 -*-
"""NLP8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11iETCeFXiebUbvMT4xA45OZf2Ap7--JF
"""

#Week 8 on Week .. 19 OCT

def myfunction(mark):
  if(mark<60):
    return 'Fail'
  else:
    return 'Pass'

myfunction(90)

myfunction(55)

#This tradtion method .. noe use ML (use input and output)

# C ..  Nearest Neighbor Algrothim 
import numpy as np # numpy >> مكتبة تمكنني من التعامل مع المصفوفات
# from heapq import nsmallest # رجع حذفه :)
def nearestNeighborAlgrothim(input,output,newinput): #اقرب جار 
  diference=[] # عرفت لست
  for i in input:
    diference.append(sum(abs(np.array(i)-np.array(newinput)))) # add الفرق between new input and input {i} .. حولتها لمصفوفة حتى يسمح لي بطرح العناصر .. 
    #newinput=[0,0]
    # [1,1]-[0,0]-[1,1]=2
    # [0,0]-[0,0]-[0,0]=0
    # [0,1]-[0,0]-[0,1]=1
    # [1,0]-[0,0]-[1,0]=1
    # diference=[2,0,1,1] so take minimum
  nearestNeighbor =min(diference)
  return output[diference.index(nearestNeighbor)]

  # another ex: input=[[100],[50],[55]] output=[1,0,0]
  # newinput=[99]
  # 100-99=1
  # 50-99=49
  # 55-99=44
  # diference=[1,49,44]
  # output=[1,0,0] so => 1

# بنشوفها وهي تشتغل
import numpy as np
def nearestNeighborAlgrothim1(input,output,newinput):
  diference=[]
  print('diference')
  for i in input:
    print(i,'-',newinput)
    diference.append(sum(abs(np.array(i)-np.array(newinput)))) 
    print(diference)
  nearestNeighbor =min(diference)
  print('least diference', nearestNeighbor)
  print('index ',diference.index(nearestNeighbor))
  print('output value ', output[diference.index(nearestNeighbor)])
  return output[diference.index(nearestNeighbor)]

input=[[100],[50],[55]]
output=[1,0,0]
new=[99]
nearestNeighborAlgrothim1(input,output,new)

input=[[100],[50],[55]]
output=[1,0,0]
new=[54]
nearestNeighborAlgrothim1(input,output,new)

input=[[100],[50],[55]]
output=[1,0,0]
new=[50]
nearestNeighborAlgrothim1(input,output,new)

# B
input=[[1,1],[1,0],[0,1],[0,0]] # function and
output=[1,0,0,0]
new=[1,1]
nearestNeighborAlgrothim(input,output,new)

# B .. b
input=[[1,1],[1,0],[0,1],[0,0]] # function or
output=[1,1,1,0]
new=[1,1]
nearestNeighborAlgrothim(input,output,new)

# A
input=[100,50,10,80]
output=[1,0,0,1]
new=[90]
nearestNeighborAlgrothim(input,output,new) #اقرب جار للنيو

input=[[100],[50],[10],[80]]
output=[1,0,0,1]
new=[60]
nearestNeighborAlgrothim(input,output,new)

input=[[100],[50],[55],[59],[60],[10],[80]]
output=[1,0,0,0,1,0,1]
new=[60]
nearestNeighborAlgrothim(input,output,new)

# ML .. امثلة يتدرب من خلالها النظام
# ما بكتب البرنامج فقط بعطيه 
# input و output التجارب السابقة
# وانا من خلال البيانات راح اعرف الشبيه واتعلم منها

# new Algorithem >> Knearst NeighborAlgrothim (KNN)

from heapq import nsmallest
import statistics
def knearestNeighborAlgrothim(input,output,newinput,k): # k >> number count, I choose it
  diference=[]
  for i in input:
    diference.append(sum(abs(np.array(i)-np.array(newinput))))
  nearestNeighbors =nsmallest(k, diference)
  print(nearestNeighbors)
  lables=[]
  for nearestNeighbor in nearestNeighbors:
    lables.append(output[diference.index(nearestNeighbor)])
    print('nearestNeighbor : ', input[diference.index(nearestNeighbor)], 'Label ', statistics.mode(lables) ) ###########
  return statistics.mode(lables)

input=[[100],[50],[55],[59],[60],[10],[80]]
output=[1,0,0,0,1,0,1]
new=[60]
count=1
knearestNeighborAlgrothim(input,output,new,count)

input=['This is great place','I enjoy my time','I hate this place']

dic={}
num=0
for i in input:
  for token in i.split():
    if(token in dic.keys()):
      print(token, 'It has been added', dic[token])
    else:
      dic[token]=num
      num=num+1

dic

# This is great place