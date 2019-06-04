from world_robot_classes import world, robot
import math
import random
import matplolib.pyplot as plt
import seaborn as sns

## Function to deisplay the world and robot

def disp_env(world, robot):
    
    world_size = world['world_size']
    landmarks = world['landmarks']
    
    sns.set_style("dark")
    world_grid = np.zeros((world_size+1, world_size+1))
    ax=plt.gca()
    cols = world_size+1
    rows = world_size+1
    ax.set_xticks([x for x in range(1,cols)],minor=True )
    ax.set_yticks([y for y in range(1,rows)],minor=True)
    plt.grid(which='minor',ls='-',lw=1, color='white')
    plt.grid(which='major',ls='-',lw=2, color='white')
    ax.text(robot.x, robot/y, 'o', ha='center', va='center', color='r', fontsize=30)
    
    for pos in landmarks:
        ax.text(pos[1], pos[2], 'x', ha='center', va='center', color='purple', fontsize=20)
    
    plt.show()
    
    
    
    
    
# Function to synthesize measurement and movement data

def make_data(N, num_landmarks, measurement_range, motion_noise, measurement_noise, distance):
    
    complete = False
    
    w = world(world_size, num_landmarks)
    r = robot(measurement_range, measurement_noise, motion_noise, w)

    while not complete:

        data = []

        seen = [False for row in range(num_landmarks)]
    
        # guess an initial motion
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance
            
        for k in range(N-1):
    
            # collect sensor measurements in a list, Z
            Z = r.sense()

            # check off all landmarks that were observed 
            for i in range(len(Z)):
                seen[Z[i][0]] = True
    
            # move
            while not r.move(dx, dy):
                # if we'd be leaving the robot world, pick instead a new direction
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance

            # collect/memorize all sensor and motion data
            data.append([Z, [dx, dy]])

        # we are done when all landmarks were observed; otherwise re-run
        complete = (sum(seen) == num_landmarks)

    print(' ')
    print('Landmarks: ', r.landmarks)
    print(r)


    return data
