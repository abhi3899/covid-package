# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:50:19 2020

@author: ABHINAV
"""
from covid import Covid
covid=Covid(source="worldometers")
data=covid.get_data() 
"""print(data)"""
country=covid.get_status_by_country_name("india")
"""print(country)"""
conf_cases=covid.get_total_confirmed_cases()
"""print(conf_cases)"""
active_cases=covid.get_total_active_cases()
"""print(active_cases)"""
total_deaths=covid.get_total_deaths()
print(total_deaths)
