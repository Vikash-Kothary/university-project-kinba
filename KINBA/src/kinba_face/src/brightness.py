import argparse
import numpy as np
import cv2

def main():
	
def test():
  image = cv2.imread(image_path)
  blur_image = cv2.medianBlur(image, 3)
  hsv_image = cv2.cvtColor(blur_image, cv2.COLOR_BGR2HSV)
  image_gray = cv2.cvtColor(full_image, cv2.COLOR_BGR2GRAY)
