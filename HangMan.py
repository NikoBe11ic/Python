name=input("Please write your name: ")
print(f"Hello Mr {name}, Let's play HangMan")

secret_word="Alastun"

guess_string=""

lives=10

while lives>0:

	character_left=0

	for character in secret_word:

		if character in guess_string:
			print(character)
		else:
			print("-")
			character_left+=1

	if character_left==0:
		print("You won")
		break



	guess=input("Please guess:")
	guess_string+=guess

	if guess not in secret_word:
		lives-=1
		print("Wrong guess")
		print(f"You have {lives} left")

		if lives==0:
			print("You died")
