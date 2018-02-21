
# coding: utf-8

# In[28]:

import urllib.request
import json
import re

tokens = []
text = ''
response = ''
owner_id = ['38940203', '129186922', '53083705']
for i in owner_id:
    req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id='+i+'&count=10&access_token=636983836369838363698383b56308ddcf663696369838339e4c9143df3f3c05ba2bc00&v=V ')
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8') 
    vk_wall = json.loads(result)
    for num in range(1,10):
        text += vk_wall['response'][num]['text'] + ' '
        tokens = re.findall('\w+', text)  
print(tokens)


# In[ ]:




# In[ ]:



