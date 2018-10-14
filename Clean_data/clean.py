# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:34:10 2018

@author: Jordane TSAFACK
"""

path = "J:/athlete_events.json"
path_sauve = "J:/good_athlete_events.json"
try:  
    file = open(path)
# lecture de du fichier
    data = file.read()

except Exception as e: 
    
    print(e.message)    

# premier prétraitement 

data_clean = data.replace("{\n", "{")
data_clean = data_clean.replace('",\n', '",')
data_clean = data_clean.replace(',\n', ',')
data_clean = data_clean.replace("\n },", "}\n")
 
# on fait un traitement particulie pour chaque ligne 
 



#==============================================================================
new_data=[]
for i, line in enumerate(data_clean.split('\n')[1:]):
    
    current_line =('{"index":{"_index": "athletesjo%d","_type":"athlete","_id":%d}}\n{ "fields" :'+line+'}')%(i+1,i+1)
    new_data.append(current_line)
   # print(i)
    
    
     
# on concatene la liste en séparant les élémnets pa run retour au chariot
data_good_formated='\n'.join(new_data)

     
 #==============================================================================

#==============================================================================
# print(data.count('}'))
# data2=data.replace('},', '}')
# 
sauve_file = open(path_sauve, 'w')
sauve_file.write(data_good_formated)
#sauve_file.write(data_clean)
print('end ')
file.close()
sauve_file.close()
#==============================================================================
