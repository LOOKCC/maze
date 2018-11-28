#!/usr/bin/env python
# coding=utf-8
import numpy as np
from environment import environment

action_dict = {'up':0, 'down':1, 'left':2, 'right':3}
def epsilon_greedy(state, action, Q_table, epsilon):
    action_index = [action_dict[x] for x in action]
    action_prob = [Q_table[4*state[0]+state[1]][x] for x in action_index]
    action_prob = np.asarray(action_prob)
    x = np.random.rand()
    if x < 1-epsilon:
        a = action[np.random.randint(0, len(action))]
    else:
        a = action[action_prob.argmax()]     
    return a


def max_reward(state, action, Q_table):
    action_index = [action_dict[x] for x in action]
    action_prob = [Q_table[4*state[0]+state[1]][x] for x in action_index]
    return max(action_prob)


def train(env, alpha, epsilon, Q_table):
    state = env.start()
    while True:
        available_action = env.get_action(state)
        action = epsilon_greedy(state, available_action, Q_table, 0.9)
        next_state, reward, end = env.get_reward(state, action)
        available_next_action = env.get_action(next_state)
        Q_table[4*state[0]+state[1]][action_dict[action]] += alpha*(reward + 
            max_reward(next_state, available_next_action, Q_table) - Q_table[4*state[0]+state[1]][action_dict[action]])
        state = next_state
        if end == True:
            break

if __name__ == "__main__":
    env = environment()
    Q_table = np.zeros((16, 4))
    for i in range(100):
        train(env, 0.1, 0.9, Q_table)
    for i in range(len(Q_table)):
        print(Q_table[i])
