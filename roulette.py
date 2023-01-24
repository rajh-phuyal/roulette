import random
from player import RoulettePlayer


class RouletteGame:
	'''
	RouletteGame handels all the game logic necessary for each player
	'''
	red_numbers = [32,19,21,25,34,27,36,30,23,5,16,1,14,9,18,7,12,3] #numbers painted in red
	black_numbers = [15,4,2,17,6,13,11,8,10,24,33,20,31,22,29,28,35,26] #numbers painted in black
	green_number = [0] #number painted in green

	def __init__(self, player):
		self.player = player
	
	def print_mat(self):
		red_color = '\033[101m'
		black_color = '\033[100m'
		green_color = '\033[102m'
		end = "\033[0m"
		print("-"*20)
		print("{}{:^20}{}\n".format(green_color, 0, end))
		for x in range(1, 37):
			if x in self.red_numbers:
				print("{}{:^6}{}".format(red_color, x, end), end=" ")
			else:
				print("{}{:^6}{}".format(black_color, x, end), end=" ")
			if x % 3 == 0:
				print("\n")
		print("-"*20)
		print("{}{:^10}{}".format(red_color, "red", end), end=" ")
		print("{}{:^9}{}".format(black_color, "black", end))
		print("\n")

	def play(self, bet_amount, user_bet_on, current_round):
		self.current_ball_hit = random.choice(self.red_numbers + self.black_numbers + self.green_number)
		if self.current_ball_hit in self.red_numbers:
			result_color = "red"
		elif self.current_ball_hit in self.black_numbers:
			result_color = "black"
		elif self.current_ball_hit in self.green_number:
			result_color = "green"
		print(f"\nYou bet on: {user_bet_on}\nBall landed on: {self.current_ball_hit} | color: {result_color}")
		if user_bet_on == "red" and self.current_ball_hit in self.red_numbers:
			self.player.balance += bet_amount
			self.winning_prompt()
		elif user_bet_on == "black" and self.current_ball_hit in self.black_numbers:
			self.player.balance += bet_amount
			self.winning_prompt()
		else:
			# if the user choose a non base 10 string, the int function throws an error,
			# so that means the user bet on the wrong color and not a number.
			try:
				if int(user_bet_on) >= 0 and int(user_bet_on) <= 36 and int(user_bet_on) == self.current_ball_hit:
					self.player.balance += (bet_amount * 36)
					self.winning_prompt()
				else:
					self.player.balance -= bet_amount
					self.losing_prompt()
			except ValueError:
				self.player.balance -= bet_amount
				self.losing_prompt()

	def cash_out(self, tip_for_dealer):
		if tip_for_dealer > 0 and self.player.balance > tip_for_dealer:
			self.player.balance -= tip_for_dealer
			print(f"\nDealer: Thank you for the tip of ${tip_for_dealer:,}.\n")
		else:
			print("Thank you, but no thank you!")

	def player_stat(self, starting_balance, current_round, player_exit):
		print("_"*20)
		if player_exit:
			print(f"Total round: {current_round}")
		else:
			print(f"Current round: {current_round}")
		print(f"Starting balance: ${starting_balance:,}")
		print(f"Current balance: ${self.player.balance:,}")
		if self.player.balance > starting_balance and player_exit:
			print(f"You won a total of: ${self.player.balance - starting_balance:,}")
		elif self.player.balance < starting_balance and player_exit:
			print(f"You lost a total of: ${starting_balance - self.player.balance:,}")
		elif current_round > 1 and self.player.balance < starting_balance and player_exit:
			print(f"You are at break even.")
		print("_"*20)

	def winning_prompt(self):
		print("*** You win ***")
		print(f"New total balance: ${self.player.balance:,}\n")
	
	def losing_prompt(self):
		print("--- You lose --")
		print(f"New total balance: ${self.player.balance:,}\n")
	
	def exit_prompt(self):
		print("Thank you for playing!")