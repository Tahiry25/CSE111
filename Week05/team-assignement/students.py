import csv

def main():
    IN_INDEX = 0
    students_dict = read_dictionary("students.csv", IN_INDEX)

    i_number = input("Please Enter I-Number (xxxxxxxxx): ")
    clean_i_number = remove_dashes(i_number)
    checked_i_number = check_i_number(clean_i_number)

    if checked_i_number.isdigit():
        if checked_i_number in students_dict:
            student_name = students_dict[checked_i_number][1]
            print(student_name)
        else:
            print("No such student")
    else:
        print(checked_i_number)

def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for item in reader:
            key = item[key_column_index]
            dictionary[key] = item

    return dictionary

def remove_dashes(text):
    new_text = text.replace('-', '')
    return new_text

def check_i_number(n):
    numb = 0
    if len(n) < 9:
        return "too few digits"
    elif len(n) > 9:
        return "too many digits"
    elif not n.isdigit():
        return 'Invalid I-Number'
    else:
        numb = n

    return numb


# Call main to start this program.
if __name__ == "__main__":
    main()