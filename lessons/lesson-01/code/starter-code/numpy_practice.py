import numpy as np # import numpy class

def find_probability(array,multiple): # takes in two parameters
    data = array.tolist() # convert array to list, since filter is not defined for array type
    data2 = filter(lambda x: find_total_multiples(x,multiple), data) # take every number in the list, if it is multiple keep in array, else filter out
    total_multiples = len(data2) # count of all multiples 
    total_count = len(data) # count of all numbers
    print (float(total_multiples)/total_count)*100 # print probability

def find_total_multiples(x,multiple): return x % multiple == 0 # returns boolean value if x is divisible by the multiple

array = np.random.randint(0,1000,500) # generage random nums with randint
find_probability(array,2) # call function