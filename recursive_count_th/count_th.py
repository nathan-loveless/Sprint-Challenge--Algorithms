'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_list = list(word)
    hasNum = False
    count = 0
    if len(word_list) != 0:
        hasNum = word_list[0].isdigit()

    print("Current word list: ", word_list)
    if hasNum:
        print("Current count is: ", word_list[0])

    # It can't have any th's if there is 0 or 1 letters
    # if len(word_list) <= 2:
    if len(word_list) == 0:
        return 0
    elif hasNum == True:
        count = int(word_list[0])

    if word_list[0].isdigit() == False:
        if word_list[0] + word_list[1] == 'th':
            word_list[0] = '1'        
            print("This is the word if digit is not stored and equal 'th': ", word_list, word_list[0])
        else:
            word_list[0] = '0'
            print("This is the word if digit is not stored and not equal 'th': ", word_list, word_list[0])

   
    th = word_list[1] + word_list[2]

    if th == 'th':
        count = int(word_list[0])
        word_list[0] = str(count + 1)
        word_list.remove(word_list[1])
    else:
        word_list.remove(word_list[1])

    count_th(''.join(word_list))

    count = int(word_list[0])
    return count