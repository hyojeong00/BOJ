# formula = input()

# if '-' in formula:
#     formula = formula.split('-')

#     result = 0
#     for i in range(len(formula)):
#         if formula[i].isnumeric() == True:
#             if i == 0:
#                 result += int(formula[i])
#             else:
#                 result -= int(formula[i])
#         else:
#           temp = formula[i].split('+')
#           result -= sum([int(i) for i in temp])
#     print(result)

# else:
#     formula = formula.split('+')
#     print(sum([int(i) for i in formula]))




fomula = input().split('-')

result = 0

result += sum([int(i) for i in fomula[0].split('+')])

for i in range(1, len(fomula)):
  result -=  sum([int(i) for i in fomula[i].split('+')])

print(result)
