import numpy as np
import matplotlib.pyplot as plt

class BrownianMotionSimulator:
    def __init__(self, arena_size=3, robot_size=0.1, speed=2, delta_t=0.2, num_steps=1000):
        # Parameter
        self.arena_size = arena_size
        self.robot_size = robot_size
        self.speed = speed
        self.delta_t = delta_t
        self.num_steps = num_steps

        # Initial position
        self.position = np.array([self.arena_size/2, self.arena_size/2])
        self.direction = np.array([self.robot_size, 0])

        # Init plot
        plt.ion()
        fig = plt.figure(figsize=(3,3))
        self.ax = fig.add_subplot(111)
        self.ax.set_xlim([0, self.arena_size])
        self.ax.set_ylim([0, self.arena_size])
        self.ax.spines['top'].set_linewidth(2)
        self.ax.spines['right'].set_linewidth(2)
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.spines['left'].set_linewidth(2)
        self.ax.axes.xaxis.set_visible(False)
        self.ax.axes.yaxis.set_visible(False)
        plt.title('Brownian Motion Simulation')

        # Init robot
        self.circle = plt.Circle(self.position, self.robot_size, color='b')
        self.ax.add_artist(self.circle)
        self.arrow = self.ax.arrow(self.position[0], 
                self.position[1], 
                2 * self.direction[0], 
                2 * self.direction[1], 
                head_length=0.2, 
                head_width=0.1,
                fc='r',
                ec='r')

    def move(self):
        '''
        Move the robot in a random direction
        '''
        next_position = self.position + self.direction * self.speed * self.delta_t
    
        if next_position[0] < self.robot_size:
            rotation_angle = np.random.uniform(0, np.pi/4)
            rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                        [np.sin(rotation_angle), np.cos(rotation_angle)]])
            self.direction = np.dot(rotation_matrix, self.direction)
        elif next_position[0] > self.arena_size - self.robot_size:
            rotation_angle = np.random.uniform(np.pi/4, 3 * np.pi/4)
            rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                        [np.sin(rotation_angle), np.cos(rotation_angle)]])
            self.direction = np.dot(rotation_matrix, self.direction)
        elif next_position[1] < self.robot_size:
            rotation_angle = np.random.uniform(0, np.pi/2)
            rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                        [np.sin(rotation_angle), np.cos(rotation_angle)]])
            self.direction = np.dot(rotation_matrix, self.direction)
        elif next_position[1] > self.arena_size - self.robot_size:
            rotation_angle = np.random.uniform(np.pi/2, np.pi)
            rotation_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)],
                                        [np.sin(rotation_angle), np.cos(rotation_angle)]])
            self.direction = np.dot(rotation_matrix, self.direction)

        self.position = self.position + self.direction * self.speed * self.delta_t

    def draw(self):
        self.circle.center = self.position
        self.arrow.remove()
        self.arrow = self.ax.arrow(self.position[0], 
                      self.position[1], 
                      2 * self.direction[0], 
                      2 * self.direction[1], 
                      head_length=0.2, 
                      head_width=0.1,
                      fc='r',
                      ec='r')

    def simulate(self):
        for i in range(self.num_steps):
            self.move()
            self.draw()
            plt.show()
            plt.pause(0.01)

if __name__ == '__main__':
    simulator = BrownianMotionSimulator()
    simulator.simulate()