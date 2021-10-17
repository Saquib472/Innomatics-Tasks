# Task_4 Q_13:
# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

def minion_game(string):
    v = 'AEIOU'
    Stuart_sc, Kevin_sc = 0, 0
    length = len(string)
    for start_idx in range(length):
        score = length - start_idx
        if string[start_idx] in v:
            Kevin_sc += score
        else:
            Stuart_sc += score
    if Stuart_sc == Kevin_sc:
        print('Draw')
    if Stuart_sc > Kevin_sc:
        print('Stuart {}'.format(Stuart_sc))
    if Stuart_sc < Kevin_sc:
        print('Kevin {}'.format(Kevin_sc))

if __name__ == '__main__':
    s = input()
    minion_game(s)