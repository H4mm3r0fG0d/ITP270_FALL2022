letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using list comprehension, the zip and dict functions to create a new dictionary, letter_to_points
letter_to_points = dict(zip(letters, points))

# Adding an element to the new letter_to_points dictionary
letter_to_points[" "] = 0

# Verify the added element
#print(letter_to_points)

# Creating a function that totals the point score for each word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.pop(letter, 0)
    return(point_total)

# Testing the word scoring function
brownie_points = score_word("BROWNIE")
#print(brownie_points)

# Scoring a game of scrabble with four players
player_to_words = {
"player1": ["BLUE", "TENNIS", "EXIT"], 
"wordNerd": ["EARTH", "EYES", "MACHINE"], 
"Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
"Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points

# Verify the scores of the players
print(player_to_points)