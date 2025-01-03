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

import re
from collections import Counter
from datetime import datetime


def main():
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Task 1: Extract all order numbers (assuming order numbers are just numbers)
    order_number_regex = r'\b\d{5,10}\b'
    order_numbers = re.findall(order_number_regex, text)
    print("Order Numbers:", order_numbers)

    # Task 2: Extract all product names
    product_name_regex = r'(?<=Product:)([A-Za-z0-9\s]+)'  # Assuming product names come after "Product:"
    product_names = re.findall(product_name_regex, text)
    print("Product Names:", product_names)

    # Task 3: Extract all prices (assuming prices are in the format $xxx.xx)
    price_regex = r'\$([0-9]+\.[0-9]{2})'
    prices = re.findall(price_regex, text)
    print("Prices:", prices)

    # Task 4: Extract all order dates (assuming dates are in the format dd/mm/yyyy)
    date_regex = r'\d{2}/\d{2}/\d{4}'
    order_dates = re.findall(date_regex, text)
    print("Order Dates:", order_dates)

    # Task 5: Find all orders for products priced over $500
    products_over_500 = [line for line in text.split('\n') if '$' in line and float(re.search(r'\$([0-9]+\.[0-9]{2})', line).group(1)) > 500]
    print("Products over $500:", products_over_500)

    # Task 6: Change the date format to DD/MM/YYYY (if needed)
    converted_dates = [datetime.strptime(date, "%d/%m/%Y").strftime("%d/%m/%Y") for date in order_dates]
    print("Converted Dates:", converted_dates)

    # Task 7: Extract product names that have more than 6 characters
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product Names with more than 6 characters:", long_product_names)

    # Task 8: Count the occurrence of each product
    product_count = Counter(product_names)
    print("Product Count:", product_count)

    # Task 9: Extract orders with prices ending in .99
    prices_ending_in_99 = [line for line in text.split('\n') if line.endswith('.99')]
    print("Orders with prices ending in .99:", prices_ending_in_99)

    # Task 10: Find the cheapest product
    cheapest_product = min(prices, key=lambda x: float(x))
    print("Cheapest Product:", cheapest_product)


if __name__ == '__main__':
    main()
