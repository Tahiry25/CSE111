def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")
    fruit_list.append('orange')
    print(f"New list: {fruit_list}")
    index = fruit_list.index('apple')
    fruit_list.insert(index, 'cherry')
    print(fruit_list)
    fruit_list.remove('banana')
    print(fruit_list)
    pop = fruit_list.pop()
    print(pop)
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)

# Call main to start this program.
if __name__ == "__main__":
    main()