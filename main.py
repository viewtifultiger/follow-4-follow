# import os
from setup import setup
from data import config
from User import User
from instagrapi import Client

setup()

USERNAME, PASSWORD = config.USERNAME, config.PASSWORD

personal = User(USERNAME, PASSWORD)

# for account in differences:

# # Check to see how long I've last followed everyone in private list
# # this needs a database
# # If they take too long to accept, stop following them. And remove them
# # user_id (from database)
# cl.user_unfollow(user_id)



# # UNFOLLOWING (find the ones I need to unfollow)
# to_unfollow = dict(following_set - followers_set)
# # Unfollow the ones who no longer follow me
# for user_id in to_unfollow:
# 	cl.user_unfollow(user_id)


# user_id = cl.user_id_from_username(ACCOUNT_USERNAME)