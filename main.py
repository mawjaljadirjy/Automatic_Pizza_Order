print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size=="S":
  if add_pepperoni== "Y":
   bill=17
  else:
    bill=15

  if extra_cheese=="Y":
    bill+=1

  print(f"your final bill is: ${bill}")
elif size=="M":
  if add_pepperoni== "Y":
   bill=23
  else:
      bill=20
  
  if extra_cheese=="Y":
    bill+=1

  print(f"your final bill is: ${bill}")

else:
  if add_pepperoni== "Y":
   bill=28
  else:
   bill=25

  if extra_cheese=="Y":
    bill+=1

  print(f"your final bill is: ${bill}")  
   




