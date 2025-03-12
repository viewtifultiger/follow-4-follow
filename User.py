from login_manager import login_user

class User:
	def __init__(self, USERNAME: str , PASSWORD: str):
		self.cl = login_user(USERNAME, PASSWORD)
		self.cl.delay_range = [29, 50]
		self.id = self.cl.user_id
