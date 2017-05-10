#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import cv2
from image_system_lecture import ImageProc


class Momentum(ImageProc):
    def process(self, mat):
        gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 10, 20)
        cont, hie = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in cont:
            m = cv2.moments(c)
            m00 = m['m00']
            if m00 != 0:
                cx = int(m['m10'] / m00)
                cy = int(m['m01'] / m00)
                ca = cv2.contourArea(c)

                cv2.drawContours(mat, [c], 0, (0, 255, 0), 1)
                # cv2.circle(mat, (cx, cy), 5, (0, 0, 255), -1)
        return mat

if __name__ == '__main__':
    Momentum.run()
