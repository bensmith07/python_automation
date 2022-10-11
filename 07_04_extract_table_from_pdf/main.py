# pip install tabula-py
import tabula

# returns a list of dataframes (with one df in the list)
table = tabula.read_pdf('weather.pdf', pages=1) 

# output dataframe to csv
table[0].to_csv('output.csv', index=False)