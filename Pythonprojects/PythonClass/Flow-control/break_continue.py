def break_statement():
   x=1
   while x<10:
      print("Hello")
      x+=1
      if x==5:
         break
break_statement()

def continue_statement():
   x=1
   while x<20:
      x+=1
      if x%2==0:#when it gets to an even number it skips and continues to the odd numbers
         continue
      print(x)
continue_statement()