# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 20:10:29 2025

@author: savin
"""

"""
Pseudo code

1) import data to data frame
2) filter for 1 customer id
3) find the max BP number
4) find the min BP number
5) subtract max and min BP to get number of months
6) find sum of interest for that customer
7) find interest for 1 month
8) find interest for 12 months
9) multiply that by 30 years to get LTV
10) create a list of all customer ids
11) loop for all customer ids
12) Add LTVs to an empty list
13) zip list customer ids and their corresponding LTVs
"""

import pandas as pd

data = pd.read_excel("C:/Users/savin/OneDrive/Desktop/Spyder projects/LTV project/5._General_-_LTV_Test_2024.xlsx", sheet_name="Data")

customer_id_list = data["CustomerId"].unique().tolist()


#start of base code
data_c1 = data[data["CustomerId"]==248401]

data_c1_min_bp = data_c1["BPnumber"].min()

data_c1_max_bp = data_c1["BPnumber"].max()

number_of_months = data_c1_max_bp - data_c1_min_bp



#total interest for a customer
sum_of_interest = data_c1["Interest"].sum()

#interest per month
interest_per_month = sum_of_interest/number_of_months

interest_per_year = interest_per_month*12

ltv = interest_per_year*30

#end of base code

def find_ltv(cust_id):
    
    data_c1 = data[data["CustomerId"]==cust_id]

    data_c1_min_bp = data_c1["BPnumber"].min()

    data_c1_max_bp = data_c1["BPnumber"].max()

    number_of_months = data_c1_max_bp - data_c1_min_bp



    #total interest for a customer
    sum_of_interest = data_c1["Interest"].sum()

    #interest per month
    interest_per_month = sum_of_interest/number_of_months

    interest_per_year = interest_per_month*12

    ltv = interest_per_year*30
    
    return ltv

ltv_list = []

for i in customer_id_list:
    
    ltv = find_ltv(i)
    
    ltv_list.append(ltv)
    
output = pd.DataFrame(list(zip(customer_id_list,ltv_list)),columns=["customer_id","ltv"])
    
    
    


