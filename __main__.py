import hideWord
import geneticAlgorithm


# FIXED_HIDDEN_WORD = 'Hey salut toi ça va ?, ça c\'est caca té d\'accord !'
# FIXED_HIDDEN_WORD = 'hellohello'

if __name__ == "__main__":
    
    try:
        FIXED_HIDDEN_WORD
    except NameError:
        print()
        FIXED_HIDDEN_WORD = ''
        while len(FIXED_HIDDEN_WORD)<1:
            FIXED_HIDDEN_WORD = input('Mot à cacher : ')

        hideWord.hide(FIXED_HIDDEN_WORD)

    geneticAlgorithm.main()