a = int(input('Enter the Starting Number: '))
b = int(input('Enter the Ending Number: '))
d=b+1
if a > b:
  print("Starting number has to be equal to or lower than ending number")
else:
  c=0
  for i in (range(a,b+1)):
      c=i+c
print('Sum of numbers from',a,'to',b,'is',c)
print('Thank You')