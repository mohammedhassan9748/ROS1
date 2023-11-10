#!/usr/bin/env python
# Importing the ROS python library that is called "rospy"
# That was added as a dependancy in the package creation 
import rospy
from std_msgs.msg import String,Int16,Bool
from v2v_msgs.msg import V2V_Example

def my_callback(car_info_received):
    # Here why we used .data and not anything else ?
    # This because if we write in the terminal
    # $ rosmsg show std_msgs/String
    # Terminal prints String data, therefore we wrote .data
    rospy.loginfo(" I heared %s",car_info_received.batteryLevel)

def listener():
    # Creating a node by initializing it by the init_node
    # and it take two arguments:
    # (1) Node Name
    # (2) Anonymous: Have 2 cases
    #       True --> I can create more than one node by using
    #                the same name bec each will have unique id
    #       False --> I can create only one node by the name 
    #                 bec it don't have unique id
    rospy.init_node('listener',anonymous=True)

    # Subscribing to the channel topic called "chatter"
    # and passing it's type of data received "String"
    # data such as:
    # (1) topic name
    # (2) Message type
    # (3) my_callback: It tells the subscriber the function
    #                  that should be executed once the
    #                  subscriber receives a string msg
    rospy.Subscriber("chatter",V2V_Example,my_callback)

    # This function keep waiting until receving a message.
    # Act as a while(1).
    rospy.spin()

#main function code
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass