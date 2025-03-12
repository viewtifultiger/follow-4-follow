import os

def setup():
	if not os.path.exists("data"):
		os.mkdir("data")
	else:
		print("DATA DIR DETECTED...")