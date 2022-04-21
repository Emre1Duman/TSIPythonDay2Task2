
Num = int(input("Enter a number "))



for i in range(1, Num+1):
  i = i - (Num//2 +1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (Num - i*2) + " "*i)
  #elif Num <= 0:
     # print("Please enter an odd number ")
