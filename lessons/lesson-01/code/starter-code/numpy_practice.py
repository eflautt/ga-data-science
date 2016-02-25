import numpy as np

def find_probability(array,multiple):
    data = array.tolist()
    data2 = filter(lambda x: find_total_multiples(x,multiple), data)
    total_multiples = len(data2)
    total_count = len(data)
    print (float(total_multiples)/total_count)*100

def find_total_multiples(x,multiple): return x % multiple == 0

array = np.random.randint(0,1000,500)
find_probability(array,2)