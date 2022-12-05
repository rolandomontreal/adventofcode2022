rawdata = ""
with open('./actualdata.txt', encoding="utf-8") as inputfile:
  rawdata = inputfile.read()

[cratesStr, instructions] = rawdata.split('\n\n')
print(cratesStr)

rows = cratesStr.split('\n')
cols = rows[-1].split()
print(cols)
stacks = {}

# Setup
rows.reverse()
rows = rows[1:]
for row in rows:
  for col in cols:
    startIndex = 1 + (int(col) - 1) * 4
    cargo = row[startIndex: startIndex+1]
    if (cargo != ' '):
      if (type(stacks.get(col)) is not list):
        stacks[col] = [cargo]
      else:
        stacks[col].append(cargo)

# Compute
for instruction in instructions.splitlines():
  splittedInstruction = instruction.split()
  iterations = int(splittedInstruction[1])
  fromColumn = splittedInstruction[3]
  toColumn = splittedInstruction[5]
  boxesToMove = []
  for i in range(0, iterations):
    # Pt 1
    # stacks[toColumn].append(stacks[fromColumn].pop())
    # Pt 2
    boxesToMove.append(stacks[fromColumn].pop())
  boxesToMove.reverse()
  stacks[toColumn].extend(boxesToMove)


# Print final result
for col in cols:
  print(stacks[col][-1])