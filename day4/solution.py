sectionAssignmentsRaw = ''
with open('./actualdata.txt', encoding="utf-8") as testdatafile:
  sectionAssignmentsRaw = testdatafile.read()

sectionAssignments = sectionAssignmentsRaw.splitlines()

totalPairs = 0
overlaps = 0
for sectionAssignment in sectionAssignments:
  bothAssignments = sectionAssignment.split(',')
  firstSplitted = bothAssignments[0].split('-')
  firstSection1 = int(firstSplitted[0])
  firstSection2 = int(firstSplitted[1])
  secondSplitted = bothAssignments[1].split('-')
  secondSection1 = int(secondSplitted[0])
  secondSection2 = int(secondSplitted[1])
  if (firstSection1 >= secondSection1 and firstSection2 <= secondSection2):
    totalPairs += 1
  elif (secondSection1 >= firstSection1 and secondSection2 <= firstSection2):
    totalPairs += 1
  if (not (firstSection2 < secondSection1 or secondSection2 < firstSection1)):
    overlaps += 1

print(f"Total pairs contained: {totalPairs}")
print(f"Overlaps: {overlaps}")