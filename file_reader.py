def read_file_to_list(filename):
    list_with_words = []
    with open(filename, "r") as file:
        reader = file.read().split("\n")
        for word in reader:
            list_with_words.append(word)
    list_with_words.remove(list_with_words[-1])
    return list_with_words
