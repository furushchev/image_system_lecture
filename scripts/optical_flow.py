#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp>

import numpy as np
import cv2
from image_system_lecture import ImageProc


class OpticalFlow(ImageProc):
    def start(self):
        self.detector = cv2.FeatureDetector_create("BRISK")
        self.prev_img = None
        self.prev_features = None
        self.max_corners = 1000
        self.colors = np.random.randint(0, 255, (self.max_corners, 3))
        
    def process(self, mat):
        gray = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
        keypoints = self.detector.detect(gray)
        pts = np.array([k.pt for k in keypoints], dtype=np.float32).reshape(-1, 1, 2)
        if pts.shape[0] > self.max_corners:
            pts = pts[:self.max_corners]
        if self.prev_img is None:
            self.prev_img = gray
            self.prev_features = pts
            return mat
        features, st, err = cv2.calcOpticalFlowPyrLK(self.prev_img, gray, self.prev_features,
                                                     None, winSize=(15,15), maxLevel=2,
                                                     criteria=(cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS,
                                                               10, 0.03))
        tracked = features[st==1]
        prev_tracked = self.prev_features[st == 1]
        for i, (c, p) in enumerate(zip(tracked, prev_tracked)):
            x0, y0 = p.ravel()
            x1, y1 = c.ravel()
            cv2.line(mat, (x1, y1), (x0, y0), self.colors[i].tolist(), 2)
            cv2.circle(mat, (x1, y1), 5, self.colors[i].tolist(), -1)

        self.prev_img = gray
        self.prev_features = pts
        return mat


if __name__ == '__main__':
    OpticalFlow.run()
