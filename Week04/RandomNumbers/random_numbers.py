import random
def main():
     words_list = ["tree", "yellow", "joy", "super"]
     numbers = [16.2, 75.1, 52.3]
     print(numbers)
     append_random_numbers(numbers)
     print(numbers)
     append_random_numbers(numbers, 3)
     print(numbers)
     print(words_list)
     append_random_words(words_list, 1)
     print(words_list)

def append_random_numbers(numbers_list, quantity = 1):
    """computes quantity pseudo random numbers called by random.uniform function"""
    num = 0
    while quantity > num:
        num += 1
        random_num = random.uniform(1, 100)
        rounded_num = round(random_num, 1)
        numbers_list.append(rounded_num)

    return numbers_list

def append_random_words(word_list, quantity = 1):
    word = 0
    add_word_list = ["girl", "gold", "table"]
    while quantity > word:
        word += 1
        random_word = random.choice(add_word_list)
        word_list.append(random_word)

    return word_list

if __name__ == "__main__":
    main()