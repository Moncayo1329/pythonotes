# Definición de la función get_choices()
def get_choices():
    # Asignación de valores a las variables
    player_choice = "rock"
    #list 
    options = ["rock" , "paper" , "scissor"]
    computer_choice = random.choice(food)
    
    # Devolver el valor de computer_choice
    return computer_choice

# Definición de la función greeting()
def greeting():
    # Devolver un saludo
    return "Hi"

# Llamada a la función greeting() y almacenamiento del resultado en la variable response
response = greeting()

# Imprimir el resultado almacenado en response
print(response)

# Dictionaries in python, are used to store data values in key value pairs 
#example 
     # heres the key and the value
dict = {"name": "beau" , "color": "blue"} 

choices = {"player": player_choice, "computer": computer_choice} 

#return choices 

#Libraries, List, Methods 

import random 

#List 
# A list in python is used to store multiple items in a single variable list are surrounded by brackets and each item is separated by a comma

food = ["pizza" , "carrots" , "eggs"] 
dinner = random.choice(food) 
