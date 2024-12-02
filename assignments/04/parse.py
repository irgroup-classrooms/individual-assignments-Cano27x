import re 


def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    regex = r'\d+'

    # Match the regex with the text
    orders = re.findall(regex, text)

    # Print the results
    print(orders)
    

if __name__ == '__main__':
    main()


#Lösung 

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
