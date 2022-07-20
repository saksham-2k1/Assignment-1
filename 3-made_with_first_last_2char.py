# program 3rd
def string_both_ends(str):
  if len(str) < 2:
    return 'Empty string'

  return str[0:2] + str[-2:]
d=input('Enter any string\n')
print(string_both_ends(d))