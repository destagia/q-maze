import random


ACTION_LIST = [(-1,0) , (1,0) , (0,-1) , (0,1)]

STATE_LIST = []
for i in range(5):
    for j in range(5):
        state = (i, j)
        STATE_LIST.append(state)

LEARNING_RATE = 0.001
DISCOUNT_RATE = 0.9

class QController(object):
    def __init__(self, maze):
        self.epsilon = 0.1
        self.__maze = maze

        # initialize tabuler Q-function
        q = {}

        for state in STATE_LIST:
            q[state] = {}
            for action in ACTION_LIST:
                q[state][action] = random.uniform(0, 0.1)

        self.q = q

    def get_random_action(self):
        dx = random.randint(-1, 1)
        if dx == 0:
            dy = random.choice([-1, 1])
        else:
            dy = 0

        return (dx, dy)

    def get_q_action(self, state):
        #
        # Select action from state
        #
        q_value = 0.0
        q_action = (0, 0)
        for action in ACTION_LIST:
            value = self.q[state][action]
            if value > q_value:
                q_value = value
                q_action = action

        return q_action

    def show_q(self):
        state = self.__maze.get_player_position()
        for action in ACTION_LIST:
            print("Q-value of action {}: {}".format(action, self.q[state][action]))

    def invoke(self):
        state = self.__maze.get_player_position()

        if random.uniform(0,1) < self.epsilon:
            action = self.get_random_action()
        else:
            action = self.get_q_action(state)

        self.__maze.move_player(action)

        if self.__maze.is_goal:
            reward = 1.0            
        else:
            reward = 0.0

        #
        # Train Q-function
        #
        state_prime = self.__maze.get_player_position()
        if self.__maze.is_goal:
            q_value_prime = 0.0
        else:
            q_value_prime = self.q[state_prime][self.get_q_action(state_prime)]

        q_value = self.q[state][action]
        self.q[state][action] = q_value + LEARNING_RATE * ((reward + DISCOUNT_RATE * q_value_prime) - q_value)





