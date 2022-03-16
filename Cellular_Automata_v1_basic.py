# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:35:43 2022

@author: KUMAR
"""

"""
    In this version, the program is taking a rule and a seed as initial_state
    to simulate for 200 generations:
    
    for the border condition, the blanks has been filled with "0" and
    the rule remains the same.
    for example, for the last bit of the seed, instead of "1", it is taken as "100"
    
    In the next version, we can apply other rules for the boundary condition.
    
    for "rule" and "seed", it can work for almost any as long as:
        the seed and rule are represented in 1 and 0.
        the factors in the rule is of length 3.
        All the 8 possibilities for rule of length 3 is defined.
        
"""

rule = {"111": '0', "110": '0', "101": '0', "000": '0',
        "100": '1', "011": '1', "010": '1', "001": '1',}

seed = '10001000000000010000000001'


"""the evolution function have 2 parts.
    In the first part, it's creating a list of all the blocks of 3 numbers,
    starting from the first bit of seed to the last. On the last bits,
    it's follwing the boundary condition mentioned above.
    
    In the second part, the objects of the list generated is being referenced 
    to the dictionary of rules and the result is presented as a string.

"""

def evolution(initial_state):
    
    patterns = [] #This is the list of all patterns in initial_state, n at a time
    
    for i in range(len(initial_state)):
        
        if i <= len(initial_state)-3:
            patterns.append(initial_state[i:i+3])
        
        elif i == len(initial_state)-2:
            block_2 = initial_state[i:i+2]
            block_2+= "0"
            patterns.append(block_2)
            
        elif i == len(initial_state)-1:
            block_1 = initial_state[i:i+1]
            block_1 += "00"
            patterns.append(block_1)
            
            
    next_state = ""   #this is the new state based on the rules

    for i in range(len(patterns)): #the objects of the list created above in patterns
        
        next_state += rule[patterns[i]]  
        
    return next_state


for i in range (200):
    
    print (evolution(seed))
    seed = evolution(seed)
    
