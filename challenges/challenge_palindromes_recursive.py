def is_palindrome_recursive(word, low_index, high_index):

    if word is None or len(word) == 0:
        print(low_index, high_index)
        return False

    if len(word) == 1 or (len(word) == 2 and word[0] == word[1]):
        return True

    if word[0] == word[-1]:
        return is_palindrome_recursive(word[1:-1], 1, 1)
    else:
        return False
