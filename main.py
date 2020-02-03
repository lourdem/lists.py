def print_indices(items):
    for item in items:
        #.index() gives you the position or index of something in a list
        position = items.index(item)
        print(item, position)


def words_in_common(words1, words2):
    for word in words1:
        #if word is also in the second list words2
        if word in words2:
            return word


# def every_other_item(items):
#     for item in items:
"""attempting to do every other item by adding +1"""
#         other = items.index(item+1)
#         return other


def smallest_n_items(items, n):
    #sort items by ascending order
    items.sort()
    #have to print only n items
    nList = items[:n]
    #sort n items (now in nList) by descending order, which is reverse
    nList.sort(reverse = True)      
    return nList