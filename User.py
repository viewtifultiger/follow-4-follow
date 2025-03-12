from login_manager import login_user

class User:
	def __init__(self, USERNAME: str , PASSWORD: str):
		# CLIENT
		self.cl = login_user(USERNAME, PASSWORD)
		self.cl.delay_range = [29, 50]


		self.user_id = self.cl.user_id

	def balance_socials(self):
		followers = self.cl.user_followers(personal_id)
		following = self.cl.user_following(personal_id)

		followers_set = set(followers.items())
		following_set = set(following.items())

		# FOLLOWING (find the one I need to follow)
		# Check to see if to_follow list has any private accounts
		# to_follow = dict(followers_set - following_set)
		# for user_id in to_follow:
		# 	if cl.user_info(user_id).dict()['is_private']:
		# 		# Keep track of time I requested to follow someone if they were private
		# 		# this needs a database
		# 	# Follow everyone in the to_follow list
		# 	username = to_follow[user_id].dict()['username']
		# 	print(f"Following: {username}")
		# 	cl.user_follow(user_id)

		to_follow = dict(followers_set - following_set)
		for user_id in to_follow:
			if not cl.user_info(user_id).dict()['is_private']:
				username = to_follow[user_id].dict()['username']
				print(f"Following: {username}")
				cl.user_follow(user_id)

		# differences = dict(followers_set ^ following_set)