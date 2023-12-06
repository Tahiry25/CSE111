import csv
from datetime import datetime

PRODUCT_INDEX = 0
SALES_TAX = 0.06
DISCOUNT = 0.10
STORE_NAME = "Alibaba Local Store"

def main():
    date = datetime.now()
    current_date = date.strftime("%a %b %d %I:%M:S %Y")

    try:
        product_dict = read_dictionary('products.csv', PRODUCT_INDEX)
    except:
        print("No such file or directory: 'products.csv'")
        return

    print(STORE_NAME)
    print("-------------------\n")
    items_total_qty = 0
    sub_total = 0
    with open('request.csv', 'rt') as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            try:
                product_name = product_dict[row_list[0]][1]
                qty = int(row_list[1])
                items_total_qty += qty
                price = float(product_dict[row_list[0]][2])
                sub_total += qty * price
                print(f"{product_name}: {qty} @ {price}")
            except:
                print(f"Error: unknown product ID in the request.csv file '{ row_list[0] }'")


    tax = sub_total * SALES_TAX
    discount = sub_total * DISCOUNT
    if date.strftime("%a") == "Tue":
        total = sub_total + tax - discount
    elif date.strftime("%a") == "Wed":
        total = sub_total + tax - discount
    else:
        total = sub_total + tax

    print(f"\nNumber of items: {items_total_qty}")
    print(f"Subtotal: {sub_total:.2f}")
    print(f"Sales Tax: {tax:.2f}")
    print(f"Total: {total:.2f}")
    print(f"\nThank you for shopping at {STORE_NAME}.")
    print(current_date)


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
    return dictionary

# Call main to start this program.
if __name__ == "__main__":
    main()