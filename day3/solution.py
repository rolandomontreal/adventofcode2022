rucksacksRaw = ''
with open('./actualdata.txt', encoding='utf-8') as file:
  rucksacksRaw = file.read();

rucksacks = rucksacksRaw.split('\n')
prioritysum = 0
for rucksack in rucksacks:
  firstBox = rucksack[0:len(rucksack) // 2]
  firstBoxSet = set(firstBox)
  secondBox = rucksack[len(rucksack) // 2: len(rucksack)]
  secondBoxSet = set(secondBox)
  intersection = firstBoxSet.intersection(secondBoxSet)
  element = intersection.pop()
  priority = 0
  if (element.isupper()):
    priority = ord(element) - 38
  else:
    priority = ord(element) - 96
  prioritysum += priority
  
print(prioritysum)


# Part 2
prioritysum = 0
for i in range(0, len(rucksacks), 3):
  rucksack1 = rucksacks[i]
  rucksack2 = rucksacks[i+1]
  rucksack3 = rucksacks[i+2]
  common = set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3))
  priority = 0
  element = common.pop()
  if (element.isupper()):
    priority = ord(element) - 38
  else:
    priority = ord(element) - 96
  prioritysum += priority
  
print(prioritysum)