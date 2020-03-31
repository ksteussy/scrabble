letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letter: point for letter, point in zip(letters, points)}
# print(letters_to_points)

letters_to_points[" "] = 0


# print(letters_to_points)

# print(letters_to_points["Z"])

def score_word(word):
    score = 0
    for letter in word.upper():
        score += letters_to_points[letter]
    return score


# print(score_word("Hound"))

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}


# print(player_to_words)


# print(player_to_points)

def play_word(player, word):
    player_to_words[player] += [word]


play_word("player1", "fish")
# print(player_to_words)


for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

#commit test