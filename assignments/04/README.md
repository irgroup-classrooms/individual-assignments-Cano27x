# Regular Expressions

In the following, you will parse information from text-based files with the command line and Unix tools and Python in the next step. Please note that even though the files are provided as structured csv files you are not supposed to simply read out the columns, but you should use regular expressions instead.

## Parsing contact information from the command line

In this directory, you will find a txt-file called `csv/contacts.csv`. Use regular expressions to extract the following information from it.

Remember that you can use different tools like `grep`, `awk`, or `sed` to use regular expressions from the command line. Pipes might also be helpful. 

You can add your command line in- and outputs directly to this README file. Alternatively, you can write a bash script with all commands and commit it to this directory.

1. Extract all email addresses from the text.
```
# Befehl zum Extrahieren der E-Mail-Adressen
grep -o -E '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' csv/contacts.csv

``` 
2. Extract all phone numbers from the text.
```
grep -o -E '(\+?\d{1,4}[-.\s]?)?(\(?\d+\)?[-.\s]?)*\d+' csv/contacts.csv


``` 
3. Extract all names that start with the letter ‘J’.
```
grep -o -E '\bJ[a-zA-Z]+' csv/contacts.csv


``` 
4. Extract all street names that contain the word 'St'.
```
grep -o -E '\b\w*St\w*\b' csv/contacts.csv


``` 
5. Extract all addresses in ‘USA’.
```
grep 'USA$' csv/contacts.csv


``` 
6. Extract the last names of all people.
```
grep -o -E '\b\w+$' csv/contacts.csv


``` 
7. Extract all email domains (part after the @ sign).
```
grep -o -E '(?<=@)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' csv/contacts.csv


``` 
8.	Extract all instances of the first name ‘David’ along with their full address (street and city).
```
grep -o -E '\bDavid\b.*\b\w+\s\w+.*\b\w+\b' csv/contacts.csv


``` 
9.	Find all entries where the phone number ends with ‘7’.
``` 
grep -o -E '\b\d*7\b' csv/contacts.csv

``` 
10.	Extract all instances of first names that end with the letter 'e'.
``` 
grep -o -E '\b\w*e\b' csv/contacts.csv

``` 

## Parsing product orders with Python

In this directory, you will find another file called `csv/orders.csv` and also a short Python script that reads the file and parses all numbers with a regular expression. Please extend the script such that it also print the following extracted text pieces.

1.	Extract all order numbers from the text. 
2.	Extract all product names.
3.	Extract all prices.
4.	Extract all order dates.
5.	Find all orders for products priced over $500. (You are allowed to use Python to filter the list.)
6.	Change the date format to DD/MM/YYYY. (Note the re.sub() method)
7.	Extract product names that have more than 6 characters.
8.	Count the occurrence of each product in the text. (You may want to use the Counter class from the collections package.)
9.	Extract the orders with prices ending in .99.
10.	Find the cheapest product. (You may want to use Python's min() method.)

Lösung: 
import re
import csv
from collections import Counter
from datetime import datetime

file_path = 'csv/orders.csv'

order_number_regex = r'\b\d{5,10}\b'  # Angenommen, Bestellnummern sind Zahlen zwischen 5 und 10 Ziffern
product_name_regex = r'(?<=Product:)([A-Za-z0-9\s]+)'  # Produkname nach dem "Product:"-Tag
price_regex = r'\$([0-9]+\.[0-9]{2})'  # Preis im Format $xxx.xx
date_regex = r'\d{2}/\d{2}/\d{4}'  # Datum im Format dd/mm/yyyy

# Funktion zum Parsen der Datei
def parse_orders():
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        all_orders = list(reader)
    
    order_numbers = []
    product_names = []
    prices = []
    dates = []
    products_over_500 = []
    long_product_names = []
    prices_ending_in_99 = []
    product_counter = Counter()

    for order in all_orders:
        order_number = order[0]  # Angenommene Position für die Bestellnummer
        product_name = order[1]  # Angenommene Position für den Produktnamen
        price = order[2]  # Angenommene Position für den Preis
        order_date = order[3]  # Angenommene Position für das Datum
        
        # Extrahiere und speichere Bestellnummern
        order_numbers.extend(re.findall(order_number_regex, order_number))
        
        # Extrahiere und speichere Produktnamen
        product_names.extend(re.findall(product_name_regex, product_name))
        
        # Extrahiere und speichere Preise
        prices.extend(re.findall(price_regex, price))
        
        # Extrahiere und speichere Daten
        dates.extend(re.findall(date_regex, order_date))
        
        # Filtere Bestellungen mit Preisen über $500
        if float(price[1:]) > 500:
            products_over_500.append(order)
        
        # Finde Produktnamen mit mehr als 6 Zeichen
        if len(product_name) > 6:
            long_product_names.append(product_name)
        
        # Finde Preise, die auf .99 enden
        if price.endswith('.99'):
            prices_ending_in_99.append(order)
        
        # Zähle Vorkommen jedes Produkts
        product_counter[product_name] += 1
    
    # Konvertiere Datum in das Format DD/MM/YYYY
    converted_dates = [datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y") for date in dates]

    # Finde das billigste Produkt
    cheapest_product = min(prices, key=lambda x: float(x[1:]))
    
    # Ausgabe der Ergebnisse
    print("Order Numbers:", order_numbers)
    print("Product Names:", product_names)
    print("Prices:", prices)
    print("Dates:", converted_dates)
    print("Products over $500:", products_over_500)
    print("Long Product Names (more than 6 characters):", long_product_names)
    print("Prices ending in .99:", prices_ending_in_99)
    print("Product Count:", product_counter)
    print("Cheapest Product:", cheapest_product)

parse_orders()

