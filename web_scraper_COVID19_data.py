from bs4 import BeautifulSoup
import urllib 
from urllib.request import urlopen
import requests
import csv
import pandas as pd
#URL of the
html = urlopen("https://www.juntadeandalucia.es/institutodeestadisticaycartografia/salud/static/resultadosProvincialesCovid_18.html5")

html_contents = html.read()
#create Soup object
soup = BeautifulSoup(html_contents, 'html.parser')

# Parse the html content
covid_table = soup.find("table",id='table_38676')


#main head
covid_table_data_head =covid_table.find("thead")
#main body from the table
covid_table_data_row =covid_table.find("tbody")



data = {}
# Get headers of table i.e., Casos covid, PDIA,
t_header_main=[]
for th in covid_table_data_head.find_all("th"):
    t_header_main.append(th.text.replace('\n', ' ').strip())
#print(t_header_main)

table_data = []


for tr in covid_table_data_row.find_all("tr"):
    header_mixed=[]
    if len(header_mixed)<=10:
        for th in tr.find_all("th"):
            header_mixed.append(th.text.replace('\n', ' ').strip())
        for td in tr.find_all("td"):
            header_mixed.append(td.text.replace('\n', ' ').strip())
        #print(header_mixed)
#print(header_mixed)
        t_row={}
        for main, mixed in zip(t_header_main,header_mixed):
            t_row[main]=mixed
    table_data.append(t_row)

#print(table_data)



# dictionary of lists   
df = pd.DataFrame(table_data)  
    
# saving the dataframe  
df.to_csv('Casos_confirmados_curados_y_fallecidos_por_COVID-19_en_la_provincia_de_Granada.csv')  







