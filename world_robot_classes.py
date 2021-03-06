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
    
    def __init__(self, world_size = 100.0, measurement_range = 30.0,
                 motion_noise = 1.0, measurement_noise = 1.0):
        self.measurement_noise = 0.0
        self.world_size = world_size
        self.measurement_range = measurement_range
        self.x = world_size / 2.0
        self.y = world_size / 2.0
        self.motion_noise = motion_noise
        self.measurement_noise = measurement_noise
        self.landmarks = []
        self.num_landmarks = 0
    
    def rand(self):
        return random.random() * 2.0 - 1.0
    
        
    def move(self, dx, dy):
        
        x = self.x + dx + self.rand() * self.motion_noise
        y = self.y + dy + self.rand() * self.motion_noise
        
        if x < 0.0 or x > self.world_size or y < 0.0 or y > self.world_size:
            return False
        else:
            self.x = x
            self.y = y
            return True
            
            
        
    def sense(self):

           
        measurements = []

        for l in range(len(self.landmarks)):
            dx, dy = self.landmarks[l][0]-self.x+self.rand()*self.measurement_noise, self.landmarks[l][1]-self.y + self.rand() * self.measurement_noise
            
            if (dx**2 + dy**2) < self.measurement_range or dy > self.measurement_range:
                measurements.append([l, dx, dy])
        
        
        return measurements

    
    def make_landmarks(self, num_landmarks):
        self.landmarks = []
        for i in range(num_landmarks):
            self.landmarks.append([round(random.random() * self.world_size),
                                   round(random.random() * self.world_size)])
        self.num_landmarks = num_landmarks
        
    def __repr__(self):
        return 'Robot: [x=%.5f y=%.5f]'  % (self.x, self.y)



