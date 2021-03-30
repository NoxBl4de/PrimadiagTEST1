# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 12:50:40 2021

@author: malco
"""

import json

class IncrementJson:
    
    def __init__(self, jsonFile):
        
        with open(jsonFile, 'r') as f:
            data = json.loads(f.read())
            
        self.fileName = jsonFile
        self.data = data
        
    def upjson(self, buton_id):
        
        btn = self.data[buton_id]
        
        btn['clicks'] += 1
        
        with open(self.fileName, 'w') as f:
            f.write(json.dumps(self.data))
            

obj = IncrementJson("buttons.json")
        
        