#!/usr/bin/env python

import roslib 
roslib.load_manifest('ssc32py')

import geometry_msgs
from geometry_msgs.msg import Quaternion

import rospy
import time, math

from ssc32py.ros_ssc32 import ROS_SSC32_Client

def testclient():
	rospy.init_node('ssc32_client')
	angle_sub = rospy.Subscriber("angles", Quaternion, move_callback)
	while not rospy.is_shutdown():
		rospy.spin()

def move_callback(data):
	base_angle = data.x
	shoulder_angle = data.y
	elbow_angle = data.z
	wrist_angle = data.w
	
	base = ROS_SSC32_Client('base')
	shoulder = ROS_SSC32_Client('shoulder')
	elbow = ROS_SSC32_Client('elbow')
	wrist = ROS_SSC32_Client('wrist')
	grip = ROS_SSC32_Client('grip')

	rospy.loginfo("Moving to position..")
    	elbow.move_angle(elbow_angle, endgroup=False)
	base.move_angle(base_angle, endgroup=False)
	shoulder.move_angle(shoulder_angle, endgroup=False)
	wrist.move_angle(wrist_angle, timesecs=3)

	while base.is_moving(): time.sleep(0.1)
	rospy.loginfo("Complete!")	
		
if __name__ == '__main__':
	try:
		testclient()
	except rospy.ROSInterruptException:
		pass
