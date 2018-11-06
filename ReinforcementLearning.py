import numpy as np
import gym
from gym.envs.registration import register as reg
import myenv

###THIS IS JUST A TEST!!!!!!!!!!!!

myenv/
    __init__.py
    myenv.py

register(
    id='MyEnv-v0',
    entry_point='myenv.myenv:MyEnv',
)

env = gym.make('MyEnv-v0')

#https://stackoverflow.com/questions/45068568/is-it-possible-to-create-a-new-gym-environment-in-openai/47132897#47132897



#env = gym.make("CartPole-v0")

done = False
cnt = 0 

observation = env.reset()

while not done:
    env.render()
    
    cnt += 1

    action = env.action_space.sample()

    observation, reward, done, _ = env.step(action)

    if done:
        break

print("game lasted",cnt,"moves")