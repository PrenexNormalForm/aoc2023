# Question 1
with open('day/01/input.txt') as f:
  sum = 0
  for line in f:
    digits = [int(char) for char in line if char.isdigit()]
    sum += digits[0] * 10 + digits[-1]
  print(f'Day 1 Question 1: {sum}')

# Question 2
digitMap = {'one': 1,
           'two': 2,
           'three': 3,
           'four': 4,
           'five': 5,
           'six': 6,
           'seven': 7,
           'eight': 8,
           'nine': 9,
           '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
with open('day/01/input.txt') as f:
  sum = 0
  for line in f:
    lineDigits = []
    for index in range(len(line)):
      for digit in digitMap:
        if line[index:].startswith(digit):
          lineDigits.append(digitMap[digit])
    sum += lineDigits[0] * 10 + lineDigits[-1]
  print(f'Day 1 Question 2: {sum}')