games = None
with open('./actualdata.txt', encoding="utf-8") as datafile:
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

def whatMoveDoIMake(myInstruction, opponentMove):
  opM = opponentMoves[opponentMove]
  if myInstruction == 'lose':
    if opM == 1:
      return 3
    elif opM == 2:
      return 1
    else:
      return 2
  elif myInstruction == 'draw':
    return opM
  else:
    if opM == 1:
      return 2
    elif opM == 2:
      return 3
    else:
      return 1

totalscore = 0
for game in games:
  moves = game.split(' ')
  myMove = moves.pop()
  opponentMove = moves.pop()
  score = 0
  # I should loose
  if myMove == 'X':
    movePoint = whatMoveDoIMake('lose', opponentMove)
    score += 0 + movePoint
  # I should draw
  elif myMove == 'Y':
    movePoint = whatMoveDoIMake('draw', opponentMove)
    score += 3 + movePoint
  # I should win
  else:
    movePoint = whatMoveDoIMake('win', opponentMove)
    score += 6 + movePoint
  totalscore += score

print(f"total score of all rounds: {totalscore}")
  
