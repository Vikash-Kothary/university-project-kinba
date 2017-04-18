#!/usr/bin/env python3
# eye.py

import rospy
from std_msgs.msg import String
# clarifai imports
from clarifai import rest
from clarifai.rest import ClarifaiApp

CLARIFAI_APP_ID = 'M-oh10e1jkWA7CbP85v0tcXAtjSybK6tmIILRb5t'
CLARIFAI_APP_SECRET = 'zwRvIaLMeZAsFBZnBHxOXV9nPJiDX1nf9nukVr0K'

def main():
	app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
	# get the general model
	model = app.models.get("general-v1.3")

	result = app.tag_images(data)['results'][0]['result']['tag']['classes']

if __name__ == '__main__':
	main()