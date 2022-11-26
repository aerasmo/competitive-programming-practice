# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Output Format

# Print one line: the name of the winner and their score separated by a space.

# If the game is a draw, print Draw.


# TRIED string.count(substring)
# TRIED defaultdict(lambda: 0)
# TRIED 2 for loops and += 1 score)
# SOL single loop because it is guaranteed it will appear)

def minion_game(string):
    # from collections import defaultdict
    # def count(string, substring):
    #     count = 0
    #     for i in range(len(string)):
    #         for j in range(i + 1, len(string) + 1):
    #             if substring == string[i:j]:
    #                 count += 1
    #     return count

    s = 0
    k = 0

    # substrings = defaultdict(lambda: 0)
    for i in range(len(string)):
        # for j in range(i + 1, len(string) + 1):
        #     substring = string[i:j]
        if string[i] in 'AEIOU': 
            k += len(string) - i
        else:
            s += len(string) - i
            # if substring not in substrings:
            # substrings[substring] += 1
                # score = count(string, substring)

    # determine winner
    if k > s:
        output = f'Kevin {k}'
    elif s > k:
        output = f'Stuart {s}'
    else:
        output = 'Draw'
    print(output)


if __name__ == '__main__':
    s = input()
    minion_game(s)