#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import pi
import time 
x=0
y=0
z=0
rotz=0
def check(msg):
	global x,y,z,rotz
	x=msg.pose.pose.position.x
	y=msg.pose.pose.position.y
	z=msg.pose.pose.position.z

def main():
	rospy.init_node("jack")
	pub1=rospy.Publisher("/cmd_vel",Twist,queue_size=10)
	sub1=rospy.Subscriber("/odom",Odometry,check)
	send=Twist()
	rate=rospy.Rate(3)
	send.linear.x=0
	send.linear.y=0
	send.linear.z=0
	send.angular.x=0
	send.angular.y=0
	send.angular.z=0
	last_time=time.time()
	while not rospy.is_shutdown():
		if(time.time()-last_time>9 and time.time()-last_time<10):
			rospy.loginfo("reached")
			notime=time.time()
			send.angular.z=pi*45/180
			send.linear.x=0
			rospy.loginfo(1)
			while(time.time()-notime<1.5) :
				pub1.publish(send)
				rate.sleep()
				rospy.loginfo(1.5)
			send.angular.z=0
			pub1.publish(send)
		elif(time.time()-last_time>14 and time.time()-last_time<15):
			send.angular.z=-(pi*0.5)
			send.linear.x=0
			notime=time.time()
			rospy.loginfo(3)
			while(time.time()-notime<1.5) :
				pub1.publish(send)
				rate.sleep()
				rospy.loginfo(3.5)
			send.angular.z=0
			pub1.publish(send)
		rospy.loginfo(2)
		send.linear.x=0.5
		send.angular.z=0
		pub1.publish(send)
		rate.sleep()

if __name__=="__main__":
	time.sleep(19)
	main()

		




