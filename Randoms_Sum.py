#Program that generates 2 random numbers and then does the sum of the following 

from fastapi import FastAPI

import random

app=FastAPI()

@app.get('/random/{limit}')
def get_random(limit:int ):
    #generates random number 1
    random_number1:int =random.randint(0,limit)
    #generates random number 2
    random_number2:int =random.randint(0,limit)
    sum:int=random_number1+random_number2
    #prints the values of both numbers along with its sum and the max limit of number genration
    return {'number1':random_number1   ,'number2':random_number2   ,'sum of both random':sum,    'limit'" ":limit}


