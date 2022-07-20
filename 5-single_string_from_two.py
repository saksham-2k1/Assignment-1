# program 5th
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
a=input('Enter value of first string\n')
b=input('Enter value of second string\n')
print(chars_mix_up(a,b))