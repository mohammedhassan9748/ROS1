#!/bin/bash
import rospy
import cv2

from std_msgs import String
from cv_bridge import CvBridge, CvBridgeError

import sys

bridge = CvBridge()

def main(args):
    rospy.init(" image converter", anonymous = True)
    sub = rospy.Subscriber('ayhaga')

