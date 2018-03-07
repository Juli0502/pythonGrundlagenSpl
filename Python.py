summe = 0
n = 1
while n <= 1000000000000000000:
  summe = summe + n
  print(n, end=",")
  n = n + 1 
  if n >= 11000000000000000000000000:
    break
  
print(summe)