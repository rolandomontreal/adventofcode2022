testdata1 = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
testdata2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
testdata3 = 'nppdvjthqldpwncqszvftbrmjlhg'
testdata4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

bufferIn = testdata4

with open('./actualdata.txt', encoding="utf-8") as inputfile:
  bufferIn = inputfile.read()

i = 0
startOfPacket = None
startOfMessage = None
while i < len(bufferIn) - 3 and (startOfPacket == None or startOfMessage == None):
  lastFourPicked = bufferIn[i:i+4]
  if (len(set(lastFourPicked)) == 4):
    startOfPacket = lastFourPicked
  # Pt 2
  if (i < len(bufferIn) - 13):
    lastFourteenPicked = bufferIn[i:i+14]
    if (len(set(lastFourteenPicked)) == 14):
      startOfMessage = lastFourteenPicked
  i += 1

print(f"start of message packet found: {startOfMessage}, end index: {i + 13}")