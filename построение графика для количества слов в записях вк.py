
# coding: utf-8

# In[66]:

import urllib.request
import json
import re

tokens = []
X = []
Y = []
text = ''
response = ''
owner_id = ['129186922']
for i in owner_id:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id='+i+'&count=200&access_token=636983836369838363698383b56308ddcf663696369838339e4c9143df3f3c05ba2bc00&v=V ')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8') 
    vk_wall = json.loads(result)
    for num in range(1,100):
        text = vk_wall['response'][num]['text'] + ' '
        tokens = re.findall('\w+', text)  
        X.append(num)
        Y.append(len(tokens))

print(X)
print(Y)

import matplotlib.pyplot as plt

# X и Y - координаты точек


plt.plot(X, Y) # рисуем график - последовательно соединяем точки с координатами из X и Y
plt.show()


