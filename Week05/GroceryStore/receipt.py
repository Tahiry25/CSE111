import csv

PRODUCT_INDEX = 0

def main():
    product_dict = read_dictionary('products.csv', PRODUCT_INDEX)
    print("All Products")
    print("------------")
    print(f"{product_dict}\n")
    print("Requested Items")
    print("---------------")
    with open('request.csv', 'rt') as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            product_name = product_dict[row_list[0]][1]
            qty = row_list[1]
            price = product_dict[row_list[0]][2]
            print(f"{product_name}: {qty} @ {price}")


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