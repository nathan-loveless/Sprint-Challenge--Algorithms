'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    word_list = list(word)

    if len(word_list) < 2:
        return count

    # It can't have any th's if there is 0 or 1 letters
    # if len(word_list) <= 2:
    if len(word_list) == 0:
        return 0
    elif word_list[0] + word_list[1] == 'th':
            count += 1

    return count + count_th(word_list[1:])