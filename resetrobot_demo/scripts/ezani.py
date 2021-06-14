#!/usr/bin/env python
#rospy is needed to program ROS with Python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
def talker():
  pub = rospy.Publisher(‘joint_states’, JointState, queue_size=10)
  rospy.init_node(‘joint_state_publisher’)
  rate = rospy.Rate(50) # 50hz is normally used
  hello_str = JointState()
  hello_str.header = Header()
#FIRST MOVEMENT
#give the six robot arm joints their names
  hello_str.header.stamp = rospy.Time.now()
  hello_str.name = [‘joint_1’, ‘joint_2’, ‘joint_3’, ‘joint_4’,‘joint_5’, ‘joint_6’]
  hello_str.position = [0.00, 0.00, -4.40, 0.00, 0.00, 0.00]
  hello_str.velocity = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
  hello_str.effort = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
  pub.publish(hello_str)
  rate.sleep()
  rospy.sleep(5)
#SECOND MOVEMENT
  hello_str.header.stamp = rospy.Time.now()
  hello_str.name = [‘joint_1’, ‘joint_2’, ‘joint_3’, ‘joint_4’,‘joint_5’, ‘joint_6’]
  hello_str.position = [0.00, 0.50, -2.00, 0.00, 0.00, 0.00]
  hello_str.velocity = [0.0001, 0.0001, 0.0001, 0.00, 0.00, 0.00]
  hello_str.effort = [0.0001, 0.0001, 0.00, 0.00, 0.00, 0.00]
  pub.publish(hello_str)
  rate.sleep()
  rospy.sleep(5)
#THIRD MOVEMENT
  hello_str.header.stamp = rospy.Time.now()
  hello_str.name = [‘joint_1’, ‘joint_2’, ‘joint_3’, ‘joint_4’,‘joint_5’, ‘joint_6’]
  hello_str.position = [0.00, -1.00, -1.40, 0.00, 0.00, 0.00]
  hello_str.velocity = [0.0001, 0.0001, 0.0001, 0.00, 0.00, 0.00]
  hello_str.effort = [0.0001, 0.0001, 0.0001, 0.00, 0.00, 0.00]
  pub.publish(hello_str)
  rate.sleep()
  rospy.sleep(5)
#FINAL MOVEMENT
  hello_str.header.stamp = rospy.Time.now()
  hello_str.name = [‘joint_1’, ‘joint_2’, ‘joint_3’, ‘joint_4’,‘joint_5’, ‘joint_6’]
  hello_str.position = [0.00, 0.00, -4.40, 0.00, 0.00, 0.00]
  hello_str.velocity = [0.00, 0.0001, 0.0001, 0.00, 0.00, 0.00]
  hello_str.effort = [0.00, 0.0001, 0.0001, 0.00, 0.00, 0.00]
  pub.publish(hello_str)
if __name__ == ‘__main__’:
  try:
      talker()
  except rospy.ROSInterruptException:
pass
