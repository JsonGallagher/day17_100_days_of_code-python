from getpass import getpass as input

print("EPIC    🪨 📄 ✂️    BATTLE ")
print()
print("Select your move: R, P S")

# init scores to 0
score_player1 = 0
score_player2 = 0

# create while loop that continues until either player wins 3 rounds
while True:
  # each player takes a turn
  p1_move = input("Player 1: What is your move? ").lower()
  p2_move = input("Player 2: What is your move? ").lower()
  
  # evaluate winner, draw, or invalid move. 
  # increment round winner score
  if p1_move == 'r':
    if p2_move == 'r':
      print("You both chose rock, the game is a draw!")
    elif p2_move == 'p':
      print("Player 1's rock is smothered by Player 2's paper.")
      score_player2 += 1
    elif p2_move == 's':
      print("Player 1's rock destroyed Player 2's scissors.")
      score_player1 += 1
    else:
      print(f"Sorry Player 2, {p2_move} is an invalid move.")
  elif p1_move == 'p':
    if p2_move == 'p':
      print("You both chose paper, the game is a draw!")
    elif p2_move == 'r':
      print("Player 1's paper smothered Player 2's rock.")
      score_player1 += 1
    elif p2_move == 's':
      print("Player 2's scissors cut up Player 1's paper.")
      score_player2 += 1
    else:
      print(f"Sorry Player 2, {p2_move} is an invalid move.")
  elif p1_move == 's':
    if p2_move == 's':
      print("You both chose scissors, the game is a draw!")
    elif p2_move == 'r':
      print("Player 2's rock destroyed Player 1's scissors.")
      score_player2 += 1
    elif p2_move == 'p':
      print("Player 1's scissors cut up Player 2's paper.")
      score_player1 += 1
    else:
      print(f"Sorry Player 2, {p2_move} is an invalid move.")
  else:
    print(f"Sorry Player 1, {p1_move} is an invalid move.")
 
  # print scores at the end of each round
  print()
  print(f"Player 1 Score: {score_player1}")
  print(f"Player 2 Score: {score_player2}")
  print()
  # eval if either player has reached 3, if so end game
  if score_player1 == 3 or score_player2 == 3:
    if score_player2 == 3:
      print("Player two won 3 rounds and wins the game. Thanks for playing!")
      exit()
    elif score_player1 == 3:
      print("Player one won 3 rounds and wins the game. Thanks for playing!")
      exit()
  else:
    continue