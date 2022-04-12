def collatz(number):
  return number // 2 if number % 2 == 0 else 3 * number + 1

num = int(input ("Enter number:- "))

while True:
  print (num)
  
  if num == 1:
    break
  else:
    num = collatz (num)
  
print ("Bye")