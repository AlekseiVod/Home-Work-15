def single_root_words(root_word, *other_words):
    lower_root = root_word.lower()
    same_words = []
    for word in other_words:
        lower_world = word.lower()
        if lower_root in lower_world or lower_world in lower_root:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
