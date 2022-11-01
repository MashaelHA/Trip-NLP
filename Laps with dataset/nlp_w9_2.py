# -*- coding: utf-8 -*-
"""NLP W9 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1woVNS5g4IIfalc0QLU3hlC7gOsQsii7w
"""

# Week 9 on Thusday

# dealling with number just >> problem

import numpy as np
def nearestNeighborAlgrothim(input,output,newinput):
  diference=[]
  for i in input:
    diference.append(sum(abs(np.array(i)-np.array(newinput)))) 
  nearestNeighbor =min(diference)
  return output[diference.index(nearestNeighbor)]

sentinces = ['Great resurant','Good Price','Bad service']
# sentincesConverted = [[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1]]
output = [1,1,-1]
dic ={
    'Great' : 0,
    'resurant' :1,
    'Good' :2,
    'Price' :3,
    'Bad' :4,
    'service' :5,
}
print('Words in the Dictionary:')
for word in dic.keys():
  print(word,dic[word])

print('==============')
print('No of words :' , len(dic.keys()))

print('==============')
sentincesConverted = []
print('start Converting text to list of zeros and ones')
for i in sentinces:
  mylist = [0]*len(dic.keys())
  print(mylist,'List now at begin')
  for token in i.split():
    print(token, dic[token])
    mylist[dic[token]] = 1
  print(mylist)
  sentincesConverted.append(mylist)
print(sentincesConverted)

newinput = 'Bad Price service'
convertedNewinput = [0]*len(dic.keys())
for i in newinput.split():
    convertedNewinput[dic[i]] = 1

print(convertedNewinput)

nearestNeighborAlgrothim(sentincesConverted,output,convertedNewinput)

# Back to yestarday code >> project 1

import pandas as pd # allow read fael csv(Comma-separated values) and put on column
import nltk
from nltk.stem.isri import ISRIStemmer # استخدمناه عشان يقلل الكلمات و المصفوفة في الديكشنري
st = ISRIStemmer()
data = pd.read_csv('/content/sample_data/CompanyReviews.csv')
# print(data) #me
# print(data.head()) #Dr #Defult head(5)

# I choose 2 column
inputs = data['review_description']
output = data['rating']
print(inputs.head())
print(output.head())

############### Reviw ############
# from NLP 8 > creeat dic ......
# dic={}
# num=0
# for i in input:
#   for token in i.split():
#     if(token in dic.keys()):
#       print(token, 'It has been added', dic[token])
#     else:
#       dic[token]=num
#       num=num+1
#################################

# يعني اني بمر على الجمل كلها وك جملة بفصلها لتوكن
# وبعجين برجع الجملة لأصلها
# to help shourt number of words
def creatDictionary(inputs):
  dic= {}
  num = 0
  for i in inputs:
    i = str(i)
    print()
    for token in i.split():
      # if(token in dic.keys()): #4620 .. try if eimlit stem
      if(st.stem(token) in dic.keys()):
        # print(token, 'It has been added', dic[token])
        pass
      else:
        # dic[token]= num #4620 .. try without stem
        dic[st.stem(token)]= num
        num = num+1
  return dic

dic = creatDictionary(inputs[0:1000])
print(len(dic)) # 2579 words 

# until now we creat dicinary
# after that convort token to number (array)




def convertInputToarray(inputs, dic):
  inputConverted = []
  for i in inputs:
    listofzeros = [0] * len(dic.keys()) #ضرب حجم القاموس اللي عندي # create list contain zoero every index
    i = str(i) # برجع الكلمة لأصلها فتأكد ان الجملة سترينق
    for token in i.split(): #يفصل الكلمات
      if(st.stem(token) in dic.keys()):
        listofzeros[dic[st.stem(token)]] = 1 # اذا موجودة التوكن بيحط مكانه واحد في الليست جملة جملة
    inputConverted.append(listofzeros)
  return inputConverted # 1000 عامود .. row = 2579 # عكست هنا :)

dic = creatDictionary(inputs[0:40000]) # بيرسل االف عنصر ف بيصير الف صف و الاعمدة يساوي عدد الكلمات
print('Words in Dicionary : ',len(dic.keys())) # ---- words
inputConverted = convertInputToarray(inputs[0:40000],dic) 





# Now can I use nearest neighborhod algorithm

######################### review ######################
import numpy as np
def nearestNeighborAlgrothim(input,output,newinput): 
  diference=[] # عرفت لست
  for i in input:
    diference.append(sum(abs(np.array(i)-np.array(newinput)))) 
  nearestNeighbor =min(diference)
  return output[diference.index(nearestNeighbor)]

##############################################################


print(nearestNeighborAlgrothim(inputConverted[0:40000], output[0:40000], inputConverted[4]))
print(inputs[4], ' Label: ', output[4])


# نخلي المستخدم يدخل الكلمات 
text = input('Enter Text')
convertedText = convertInputToarray([text],dic)
print(convertedText[0]) #output[convertedText[0]]
nearestNeighborAlgrothim(inputConverted[0:40000], output[0:40000], convertedText[0])