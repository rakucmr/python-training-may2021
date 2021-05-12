# Write a function filter_short_words(word_list, n) that returns the words in
# word_list shorter than n. Use filter built-in function.
def filter_short_words(word_list, max_length):
    # def check_length(word):
    #     return len(word) < max_length
    # return filter(check_length, word_list)
    return filter(lambda word: len(word) < max_length, word_list)


# Write a function that receives any number of strings and returns
# the list of unique strings ordered by number of appearances
# (most frequent → least frequent). Use sorted built-in function.
def sort_words(*words):
    # return sorted(set(words), key=lambda word: words.count(word), reverse=True)
    return sorted(set(words), key=words.count, reverse=True)


if __name__ == '__main__':
    str_list = ['hello', 'there', 'hello', 'hi', 'hi', 'hello', 'bye']
    for short_word in filter_short_words(str_list, 4):
        print(short_word)

    # Given a list of tuples (product, price_eur), build the list of
    # (product, price_ron), knowing that the exchange rate is 4.75.
    # Use map built-in function.
    products = [('apples', 1.5), ('bananas', 2), ('pears', 3)]
    for product in map(lambda tup: (tup[0], tup[1] * 4.75), products):
        print(product)

    for elem in sort_words(*str_list):
        print(elem)
