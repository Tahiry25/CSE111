def main():
    provinces = read_file("provinces.txt")
    print(provinces)

    # # remove 1st element
    provinces = remove_first_element(provinces)
    # print(provinces)

    # # remove last element
    provinces =  remove_last_element(provinces)
    # print(provinces)

    # replace AB with Alberta
    swappedAB = replace_AB(provinces)
    # print(swappedAB)

    # Count Alberta
    count = count_alberta(swappedAB)
    print(f"\nAlberta occurs {count} times in the modified list.")

def read_file(file):
    text = []
    with open(file, 'rt') as text_file:
        for line in text_file:
            text.append(line.strip())
    return text

def remove_first_element(list):
    list.pop(0)
    return list

def remove_last_element(list):
    length = len(list)
    list.pop(length - 1)
    return list

def replace_AB(list):
    new_list = []
    for el in list:
        item = el.replace('AB', 'Alberta')
        new_list.append(item)
    return new_list

def count_alberta(list):
    count = 0
    for el in list:
        if 'Albert' in el:
            count += 1
    return count



# Call main to start this program.
if __name__ == "__main__":
    main()