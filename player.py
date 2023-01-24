

class RoulettePlayer:

	def __init__(self, player_name, balance, **kwargs):
		self.player_name = player_name
		self.risk_profile = kwargs["risk_profile"]
		self.balance = balance

