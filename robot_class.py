# ## Tthe world class which generates the world and its landmarks
# ## the robot class, which contains robots attributes and methods for navigating and sensing the world

import math
import random

class world:
    def __init__(world_size=10, num_landmarks=3):
        self.num_landmarks = num_landmarks
        self.world_size = world_size
        self.landmarks = []
        for i in range(n_landmarks):
            landmark_y, landmark_x = round(random.rand()*world_size), round(random.rand()*world_size)
            
            self.landmarks.append([i, landmark_x, landmark_y])
            
        return {'world_size': self.world_size, "landamarks":self.landmarks}


class robot:
    
    def __init__(self, sensor_range=100, sensor_noise=2, actuator_noise=2, world):
        #robot's sensor and actuator are assumed to have noise, which affects the robot's state and measurements
        # the robot is also assumed to be initially at the world's center point
        
        self.world_size = world['world_size']
        self.sensor_range = sensor_range
        self.sensor_noise = sensor_noise
        self.actuator_noise = actuator_noise
        self.x, self.y = self.world_size/2, self.world_size/2
        
    def move(x_steps, y_steps):

        self.x += x_steps + random.random()*self.actuator_noise
        self.y += y_stpes + random.random()*self.actuator_noise
        
        if self.x >= self.world_size/2:
            self.x = self.world_size/2
        else if self.x <= 0:
            self.x = 0
            
        if self.y >= self.world_size/2:
            self.y = self.world_size/2
        else if self.y <= 0:
            self.y = 0
            
            
        
    def sense():

        

    

        
