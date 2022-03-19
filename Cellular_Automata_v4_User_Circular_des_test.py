# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 19:28:41 2022

@author: KUMAR
"""

rule = {"111": '0', "110": '0', "101": '0', "000": '0',
        "100": '1', "011": '1', "010": '1', "001": '1'}

#This is the rule this program uses for simulation.




############ Function "unit_patterns" start #################
"""
    
    The function "unit_patterns" creates list of the individual units in
    the initial_state.
    It takes in 'initial_state' as parameter and returns the created list as 'patterns'
    Basically, It runs through the initital_state from
    1st bit to the last bit, that is as many times as the length of the initial_state,
    and makes a list of every bits with their neighbours.
    For example: for initial_state = "12345"
    The unit blocks are ['123', '234', '345', '451', '512']
    
    Circular boundary has been followed in this case. That's why in the example
    above, after 5 the next bit is 1.
    
    
    It's important to note that we are applying the boundary condition at the
    end in this case and not in the start.
    If we apply it from the start as well, the first element of the list will
    be '512' and this may change the sequence of the final output depending on
    the defined rule.
    
    Update: An another function with same name 'unit_patterns' has been added in which
    the cicular rule is applied both at the start and at the end.
    That is using this second version, the unit blocks discussed above will be
    ['512', '123', '234', '345', '451']
    
    Basically, either way the items of the list will remain the same, with only change being
    the last item of the list becomes first item.
    
    But the result in terms of binary will be same for this purpose. That is;
    11001 indicates 3 live(1) and 2 dead(0) in that generation and so does, 11100 and 00111 and 10011 etc.

"""


### This function has been commented out. The second version mentioned below is active.
'''
def unit_patterns(initial_state):
    
    patterns = [] #This blank list will store all the created patterns
    
    for i in range(len(initial_state)): #it will run for all the bits of the initial_state
        
        if i <= len(initial_state)-3:   #for bits with 2 available succedding bits 
            patterns.append(initial_state[i:i+3]) #first 3 bits of initial_state are appended as item to the list
        
        elif i == len(initial_state)-2: #for bit with only one available succedding bit
            block_2 = initial_state[i:i+2] #block_2 becomes a string of the two avilable bits
            block_2+= initial_state[0] #the first bit of initial_output is added as the next bit thus, circular
            patterns.append(block_2) #the final pattern 'block2' is appended as item to the list
            
        elif i == len(initial_state)-1: # for bit with no succedding bit
            block_1 = initial_state[i:i+1] # block_1 becomes of a string of the one bit
            block_1 += initial_state[0:2] # the first and second bit of initial_output is added as the next two bits
            patterns.append(block_1) #the final pattern 'block1' is appended as item to the list
    return patterns


########## test of function 'unit_patterns'  #############


def test_unit_patterns():
    
    assert unit_patterns ("1234567") == ['123', '234', '345', '456', '567', '671', '712']
    assert unit_patterns ("") == []
    assert unit_patterns ("01") == ['010', '101']
    
#test_unit_patterns()


#################### Function 'unit_patterns' end ############
'''



####################### Function 'unit_patterns' with circular boundary at start and end ########################

def unit_patterns(initial_state):
    
    patterns = [] #This blank list will store all the created patterns
    
    for i in range(len(initial_state)): #it will run for all the bits of the initial_state
        
        
        if i != 0 and i != (len(initial_state)-1):
            patterns.append(initial_state[i-1:i+2])
        
        elif i == 0:
            block_first = initial_state[-1]
            block_first += initial_state[0:2]
            patterns.append(block_first)
            
        elif i == (len(initial_state)-1):
            block_last = initial_state[i-1:i+2]
            block_last += initial_state[0]
            patterns.append(block_last)
            
            
            
    return patterns


################ Test for this version of 'unit_patterns' ################

def test_unit_patterns():
    
    assert unit_patterns ("1234567") == ['712', '123', '234', '345', '456', '567', '671']
    assert unit_patterns ("") == []
    assert unit_patterns ("01") == ['101', '010']
        
        
 ######################## Funtion 'unit_patterns' version 2 end ####################################








################## Function 'next_state' Start ##########################
"""
    The function next_state takes in 'initial_state' as parameter,
    first generates the list of all pattern blocks in 'initial_state'
    using function 'unit_patterns' and saves it in 'all_patterns'
    
    Then for all the items of list 'all_patterns', it references to the dictionary
    named 'rule' defining the rules and outputs the result as a new string as 'new_state'
    The 'new_state' is of the same length as 'initial_state'
    
"""
def next_state(initial_state): #the parameter is required by the other function inside.
    
    
    all_patterns = unit_patterns(initial_state) #the result of function 'unit_patterns' is saved as list 'all_patterns'
    #print (all_patterns)
    
    new_state = ""  #this is a empty string for new state which will be generated in the next steps
    
    for i in range(len(all_patterns)): # it runs for every item of list 'all_patterns'
        
        new_state += rule[all_patterns[i]] #the result from dict rule for the list item is added as string to the empty string
        
    return new_state #the new_state is returned which will be of the same length as initial_state



######### Test of Function 'next_state' ############

def test_next_state():
    
    assert next_state("0000") == "0000"
    assert next_state("") == ""
    assert next_state("111") == "000"

#test_next_state()

######################## Function 'next_state end #########################





############### Function 'game_of_life' Start #################


"""
    The function 'game_of_life' takes in 'seed' and 'num' as parameter.
    The seed will be feed to the function 'next_state' as parameter.
    The num defines the number of times the simulation runs for.
    
    This function doesn't 'returns' anything but prints the return value of
    'next_state' function which is iterated for 'num' times.
"""

def game_of_life(seed, num): #takes seed and num as parameters
      
    for i in range(num): #num times the simulation runs
        
        evolved_state = next_state(seed) # the output of next_state function for parameter 'seed' is saved as evolved_state
        print (evolved_state) # the output 'evolved_state' is printed
        seed = evolved_state # the evolved_state is supplied as 'seed' i.e, 'initial_state' to the function 'next_state' on every new iteration 
    
        
    ###### Test of function 'game_of_life' ##########
        
#def test_game_of_life():
    
    #function game_of_life is not returning anything but just printing
    #look for how can it be tested expect for manual testing


############# Function 'game_of_life End #####################################







################### Function 'start_program' Start  #########################

"""
    The function 'start_program' initiates the whole program.
    First it asks for 'seed' and 'num' value from the user.
    These variables are supplied as the parameter to the function 'game_of_life'.
"""
                  
def start_program():
    
    print("This is the game of life based on rule 30. Let's Play!")
    seed = input("Define the initial state of the system. Use only 0 and 1.\nEnter the seed value: ")
    num = int(input("Enter the number of times to run the simulation: "))
    
    game_of_life(seed, num)
           


start_program()
