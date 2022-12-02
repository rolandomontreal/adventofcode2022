testdata = ""
with open('./actualdata.data', encoding="utf-8") as file:
  testdata = file.read()

splittedByGroup = testdata.split('\n\n');

summed = []
for calorigroup in splittedByGroup:
  stringValues = calorigroup.split('\n')
  intValues = list(map(int, stringValues))
  summedCalories = sum(intValues)
  summed.append(summedCalories)
summed.sort()

print(summed)

highest = summed.pop()
secondHighest = summed.pop()
third = summed.pop()

sum = highest + secondHighest + third

print(f"The highest value: {highest}")
print(f"The second highest value: {secondHighest}")
print(f"The third highest value: {third}")
print(f"The sum is: {sum}")