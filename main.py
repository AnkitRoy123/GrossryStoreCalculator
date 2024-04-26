sum=0
history = []
i=0
while True :
	number = input("Enter the item price or press q to quit: \n")
	if number != "q":
		sum += int(number)
		print(f"Order total so far: {sum}.")
		history.append(sum)
  else:
		print("Thanks for using our Calculator.")
		print(f"Your total sum is {sum}.")
		break
print("Your list is",end="\n")
for element in history :
	i += 1
	print(i,end=".")
	print(element)
