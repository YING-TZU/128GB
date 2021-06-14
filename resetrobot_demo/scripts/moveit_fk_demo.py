#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019 Wuhan PS-Micro Technology Co., Itd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy, sys
import moveit_commander

class MoveItFkDemo:
    def __init__(self):
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_demo', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        arm = moveit_commander.MoveGroupCommander('arm')
        
        # 设置机械臂运动的允许误差值
        arm.set_goal_joint_tolerance(0.001)

        # 设置允许的最大速度和加速度
        arm.set_max_acceleration_scaling_factor(0.5)
        arm.set_max_velocity_scaling_factor(0.5)
        
        # 控制机械臂先回到初始化位置
        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)

        joint_positions = [-0.240345, 0.554449, -0.470743, -1.508209, -1.400018, 0.193902]
        joint_positions_2 = [-0.340345, 0.554449, -0.470743, -1.508209, -1.400018, 0.193902]
        joint_positions_3 = [-0.440345, 0.554449, -0.470743, -1.508209, -1.400018, 0.193902]
        joint_positions_4 = [-0.540345, 0.554449, -0.470743, -1.508209, -1.400018, 0.193902]
        arm.set_joint_value_target(joint_positions)
        arm.set_joint_value_target(joint_positions_2)
        arm.set_joint_value_target(joint_positions_3)
        arm.set_joint_value_target(joint_positions_4)

        arm.go()
        rospy.sleep(1)

        arm.set_named_target('home')
        arm.go()
        rospy.sleep(1)

        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)




if __name__ == "__main__":
    try:
        MoveItFkDemo()
    except rospy.ROSInterruptException:
        pass
