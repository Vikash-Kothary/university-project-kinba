#!/usr/bin/env python
# looking.py - Recongnise items that indicate weather

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

CLARIFAI_APP_ID = 'M-oh10e1jkWA7CbP85v0tcXAtjSybK6tmIILRb5t'
CLARIFAI_APP_SECRET = 'zwRvIaLMeZAsFBZnBHxOXV9nPJiDX1nf9nukVr0K'

def main():
	app = ClarifaiApp(CLARIFAI_APP_ID, CLARIFAI_APP_SECRET)
	rospy.init_node('looking', anonymous=False)
	rospy.Subscriber("/camera/rgb/image_rect_color", Image, subscribe)

def subscribe(image):
	cv2.imwrite('image.jpg', CvBridge().imgmsg_to_cv2(image, 'bgr8'))
	results = app.tag_images(data)['results'][0]['result']['tag']['classes']

	pub = rospy.Publisher('results', String, queue_size=10)
	pub.publish(result)
	if target in results:
		rospy.sleep(1)
		r = rospy.Rate(10)
		print('I found the {0}'.format(target))

if __name__ == "__main__":
	while not rospy.is_shutdown():
		main()
		rospy.spin()