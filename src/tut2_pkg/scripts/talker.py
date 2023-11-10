#!/usr/bin/env python
# Importing the ROS python library that is called "rospy"
# That was added as a dependancy in the package creation 
import rospy
# From the "msg" folder from the std_msgs library we will 
# import the String data type 
from std_msgs.msg import String
from v2v_msgs.msg import V2V_Example

def talker():
    # Creating a variable called pub that holds the Publisher
    # data such as:
    # (1) topic name
    # (2) Message type
    # (3) Queue size: The max size of the data that can be
    #     buffered and if not received they will be removed 
    #     from the first till the last in the queue.
    pub = rospy.Publisher('chatter',V2V_Example,queue_size=10)

    # Creating a node by initializing it by the init_node
    # and it take two arguments:
    # (1) Node Name
    # (2) Anonymous: Have 2 cases
    #       True --> I can create more than one node by using
    #                the same name bec each will have unique id
    #       False --> I can create only one node by the name 
    #                 bec it don't have unique id
    rospy.init_node('talker',anonymous=True)

    # Example on creating my own custom message where v2v_topic
    # is called chatter for example
    # (1) Define your message name
    my_car_info = V2V_Example()
    my_car_info.batteryLevel = 0.95
    my_car_info.id = 1223
    my_car_info.car_pose.x = 5
    my_car_info.car_speed.linear.x = 30

    # I will send this messege continously, therefore we have to 
    # define thae rate by which we will send the message.
    rate = rospy.Rate(FREQUENCY) #10hz

    while not rospy.is_shutdown():
        # Concatinating 2 strings together by this formate
        # "<string 1> %s" % <string 2> 
        hello_str = "hello world %s" % rospy.get_time()
        
        # Printing the data I need to publish on the screen
        # I can replace it with the normal python print 
        rospy.loginfo(hello_str)
        
        # The Publisher has a method called publish, it will
        # publish the message according to the type choosen
        ########pub.publish(hello_str)########
       
        # publish data of the "my_car_info"
        pub.publish(my_car_info)
        
        # Waiting for the data to be publish by the choosen 
        # rate 1/10hz = 100 ms
        rate.sleep()

#main function code
if __name__ == '__main__':
    try:
        global FREQUENCY
        FREQUENCY = rospy.get_param("freq")
        talker()
    except rospy.ROSInterruptException:
        pass