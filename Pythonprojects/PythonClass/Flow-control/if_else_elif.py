odd=range(10)
for i in odd:
    if i%2!=0:
      print(i)

def divisible_by_Five(num):
  y=range(100)
  for i  in x:
   if i %5:
      print(f'{i} is divisible by 5')
   else:
      print(f'{i}is not divisible by 5')

def multiple_comparisons():
   x=range(30)
   for i in x:
      if i%2==0:
         print(f"{i} is divisible by 2")
      elif i%3==0:
         print(f"{i} is divisible by 3")
      elif i%5==0:
         print(f"{i} is divisible by 5")
      else:
         print(f"{i} is not divisible by 2,3 and 5")
multiple_comparisons() 

def divisible_by_2_and_3():
   x=range(30)
   for i in x:
      if i%2==0 and i%3==0:
         print(f"{i} is divisible by 2 and 3")
      elif i%3==0 or i%2==0:
         print(f"{i} is divisible by either 2 or 3")
      else:
         print(f"{i} is not divisible by 2 and 3 ")
divisible_by_2_and_3()
