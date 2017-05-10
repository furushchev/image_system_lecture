#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import cv2
import re
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageProc(object):
    first_cap_re = re.compile('(.)([A-Z][a-z]+)')
    all_cap_re = re.compile('([a-z0-9])([A-Z])')

    def __init__(self, topic_name="/image_raw"):
        self.cv_bridge = CvBridge()
        self.start()
        self.sub = rospy.Subscriber(topic_name, Image, self.image_cb, queue_size=1)

    @classmethod
    def snake(cls, name):
        s1 = cls.first_cap_re.sub(r'\1_\2', name)
        return cls.all_cap_re.sub(r'\1_\2', s1).lower()

    @classmethod
    def run(cls):
        rospy.init_node(cls.snake(cls.__name__))
        cls()
        rospy.spin()


    def image_cb(self, msg):
        try:
            mat = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            rospy.logerr(str(e))
            return
        ret = self.process(mat)
        cv2.imshow(self.snake(type(self).__name__), ret)
        key = cv2.waitKey(1)
        if key >= 0:
            rospy.signal_shutdown('shutdown')

    def start(self):
        pass

    def process(self):
        NotImplementedError()
