letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
           "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Dictionary to know the value of each letter
letter_to_points = {key:value for key, value in zip(letters, points)}

#Calculate how much each word is worth in points
def score_count(word):
    points = 0
    for letter in word:
        points += letter_to_points.get(letter, 0)
    return points

#Playes and words played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "player2": ["EARTH", "EYES", "MACHINE"], 
                   "player3": ["ERASER", "BELLY", "HUSKY"], "player4": ["ZAP", "COMA", "PERIOD"]}

#Mapping of players to how many points scored
player_to_points = {}
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_count(word)
    player_to_points[player] = player_points

print(player_to_points)