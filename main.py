# import os
from setup import setup
from data import config
from instagrapi import Client
from login_manager import login_user

setup()

USERNAME, PASSWORD = config.USERNAME, config.PASSWORD

cl = login_user(USERNAME, PASSWORD)
cl.delay_range = [29, 50]
print("Login successful...")

personal_id = cl.user_id

# followers = cl.user_followers(personal_id)
# following = cl.user_following(personal_id)

# followers_set = set(followers.items())
# following_set = set(following.items())

# differences = dict(followers_set ^ following_set)
# for account in differences:



# # Check to see how long I've last followed everyone in private list
# # this needs a database
# # If they take too long to accept, stop following them. And remove them
# # user_id (from database)
# cl.user_unfollow(user_id)

# # FOLLOWING (find the one I need to follow)`
# # Check to see if to_follow list has any private accounts
# to_follow = dict(followers_set - following_set)
# for user_id in to_follow:
# 	if cl.user_info(user_id).dict()['is_private']:
# 		# Keep track of time I requested to follow someone if they were private
# 		# this needs a database
# 	# Follow everyone in the to_follow list
# 	username = to_follow[user_id].dict()['username']
# 	print(f"Following: {username}")
# 	cl.user_follow(user_id)

# # UNFOLLOWING (find the ones I need to unfollow)
# to_unfollow = dict(following_set - followers_set)
# # Unfollow the ones who no longer follow me
# for user_id in to_unfollow:
# 	cl.user_unfollow(user_id)


# user_id = cl.user_id_from_username(ACCOUNT_USERNAME)