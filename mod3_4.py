def single_root_words(root_word, *other_words) :
    same_words = []
    for pred_word in other_words:
        if root_word.lower().count(pred_word.lower()) + pred_word.lower().count(root_word.lower())>0 :
            same_words.append(pred_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)