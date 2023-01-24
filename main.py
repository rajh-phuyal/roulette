from roulette import RouletteGame
from player import RoulettePlayer


def get_player_info():
	player_name = input("Hey Gambler, What is your name?: ")
	if not player_name:
		player_name = "Panda"
	total_balance = 0
	while True:
		try:
			total_balance = int(input("Buy chips for (minimum is $10): $"))
			if total_balance < 10:
				print(f"Invalid! Cannot buy chips for: ${total_balance}\n")
				continue
			else:
				break
		except ValueError:
			print(f"Invalid! Please enter a number!\n")
	return player_name, total_balance

def get_new_bet(game):
	print("Place a bet (1, 2 or 3): \n[1] - red \n[2] - black\n[3] - 0-36\n[other] - exit")
	bet_on = "Nothing"
	while True:
		try:
			bet_on = int(input(">> "))
			break
		except ValueError:
			print(f"Sorry, cannot bet on {bet_on}. Try again")
	if bet_on == 1:
		bet_on = 'red'
	elif bet_on == 2:
		bet_on = 'black'
	elif bet_on == 3:
		bet_on = -1
		while True:
			try:
				bet_on = int(input("Choose a number between 0 - 36: "))
				if bet_on >= 0 and bet_on <= 36:
					break
				else:
					print("Inavlid!! Please choose a number between 0 - 36.")
			except ValueError:
				print("Please choose a number between 0 - 36.")
	else:
		return False, False # PLAYER DECIDED TO EXIT
	while True:
		try:
			bet_amount = int(input("Please choose an amount to bet (minimum bet is $10): $"))
			while (bet_amount > game.player.balance or (game.player.balance - bet_amount) < 0 or bet_amount < 10):
				bet_amount = int(input(f"\nInvalid amount choosen!! Your current balance is ${game.player.balance:,}\
				\nMinimum bet is $10.\nPlace a new bet amount (minimum bet is $10): $"))
			break
		except ValueError:
			print("Please enter a number!")
	
	return bet_amount, bet_on

if __name__ == "__main__":
	print("******* House Always Wins Casino *******\n")
	player_name, starting_balance = get_player_info()
	player = RoulettePlayer(player_name, starting_balance, risk_profile="low")
	r = RouletteGame(player)
	print(f"Welcome, {player.player_name}!")
	current_round = 1
	while True:
		r.print_mat()
		r.player_stat(starting_balance, current_round, player_exit=False)
		bet_amount, bet_on = get_new_bet(r)
		if not bet_amount:
			break
		r.play(bet_amount=bet_amount, user_bet_on=bet_on, current_round=current_round)
		if player.balance < 10:
			print("You ran out of money :(")
			break
		while True:
			try:
				play = int(input("Please choose (1 or 2):\n[1] - to continue\n[2] - to cash out\n>>"))
				break
			except ValueError:
				play = int(input("Invalid!\nPlease choose:\n[1] - to continue\n[2] - to cash out\n>>"))
		if play == 1:
			current_round += 1
			continue
		else:
			try:
				tip = int(input("Tip the dealer (enter 0 if not necessary): $"))
			except ValueError:
				tip = 0
			r.cash_out(tip_for_dealer=tip)
			break
	r.player_stat(starting_balance, current_round, player_exit=True)
	r.exit_prompt()