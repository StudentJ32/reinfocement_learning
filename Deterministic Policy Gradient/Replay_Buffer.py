#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 21:07:30 2018

@author: jason
"""

import numpy as np
import random
from collections import deque

class replay_buffer(object):
    def __init__(self, data_size):
        self.data_size = data_size
        self.data = deque()

    def add(self,new_data):
        self.data.append(new_data)
        if len(self.data)>self.data_size: #delete first data set
            self.data.popleft()

    def clear(self):
        self.data = deque()
    
    def batch(self,batch_size):
        data_batch = []
        if len(self.data)<=batch_size:
            data_batch= self.data
        else:
            data_batch=random.sample(self.data,batch_size)
        #print(data_batch)
        state_batch,action_batch,td_target_batch= [],[],[]
        for _ in data_batch:
            state_batch.append(_[0])
            action_batch.append(_[1])
            td_target_batch.append(_[2])
        return state_batch,action_batch,td_target_batch
