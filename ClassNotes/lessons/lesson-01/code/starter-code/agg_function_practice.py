import pandas as pd # only pandas objects will be used in this script, thus no np objects used. 

def build_data_frame( cities, states, city_avg_incomes, city_populations ): 
    city_table = pd.DataFrame( {'cities': cities,  
                                'states': states, 
                                'city_avg_incomes':city_avg_incomes, 
                                'city_populations':city_populations 
                               } ) 
    
    # if all columns are stored in a pandas series or a np array, you do not need to specify index. 
    # index is default ascending
    
    city_table.dtypes # get the dataFrame schema
    city_table.describe() # get basic dF column statistics 
    return city_table # table has default incremented index

def get_aggregate_mean(x): return x.mean()

def get_aggregate_stats(city_table):
    pop_in_millions = city_table['city_populations'].apply(lambda x: float(x)/1000000) # transform columns to correct units
    income_in_k = city_table['city_avg_incomes'].apply(lambda x: float(x)/1000)
    
    city_table['city_populations'] = pop_in_millions # append columns
    city_table['city_avg_incomes'] = income_in_k
    
    cty_table_by_state = city_table.groupby('states') # dont repeat groupBy
    
    avg_city_income_by_state = cty_table_by_state.apply(lambda x: get_aggregate_mean(x['city_avg_incomes'])) 
    
    # with cities grouped by state now, we have all the records associated with the same state
    # afterwards, with all the groups, get the mean of there city_avg_incomes grouped records
    
    avg_city_pop_by_state    = cty_table_by_state.apply(lambda x: get_aggregate_mean(x['city_populations']))
                                                              
    print(avg_city_income_by_state)
    print(avg_city_pop_by_state)
    
    # this function does not return anything, calling get_aggregate_stats will only print aggregate stats
    
# data below is all stored from the Series class from pandas package 

states = pd.Series(['GA','GA','GA','GA','GA',"NY","NY","NY","FL","FL"])
cities  = pd.Series(['Atlanta','Lilburn','Athens','Auburn','Augusta','NYC','Buffalo','Albany','Miami','Tallahassee'])
city_avg_incomes = pd.Series([55000,40000,50000,45000,30000,60000,57000,56000,65000,40000])
city_populations = pd.Series([5000000,250000,100000,50000,200000,6000000,3000000,400000,4000000,5000000])
city_table = build_data_frame( cities, states, city_avg_incomes, city_populations )
get_aggregate_stats(city_table)
