games = None
with open('./testdata.txt', encoding="utf-8") as datafile:
  data = datafile.read()
  games = data.split('\n')

myMoves = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

opponentMoves = {
  "A": 1,
  "B": 2,
  "C": 3
}

def result(myMove, opponentMove):
  myM = myMoves[myMove]
  opM = opponentMoves[opponentMove]
  if myM == opM:
    return 3
  elif (myM == 1 and opM == 2) or (myM == 2 and opM == 3) or (myM == 3 and opM == 1):
    return 0
  else:
    return 6

totalscore = 0
for game in games:
  moves = game.split(' ')
  myMove = moves.pop()
  opponentMove = moves.pop()
  score = result(myMove, opponentMove);
  if myMove == 'X':
    score += 1
  elif myMove == 'Y':
    score += 2
  else:
    score += 3
  totalscore += score

print(f"total score of all rounds: {totalscore}")
  
