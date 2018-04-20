import gym
import numpy as np
import threading

env = gym.make('Ant-v1')
observation = env.reset()
reward = 0
done = False

policy = np.random.rand(8,111)

best = None
best_policy = policy

a = 0.1
b = 0.9
rate = 0.5

it = 0.0

NUM_GUYS = 8

def run_guy(env,params):
    total_reward = 0
    ob = env.reset()
    for i in range(1,100):
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            break
    return total_reward

def mutate(params,rate):
    return params*(1-rate) + np.random.rand(*params.shape)*rate

guys_params = [None] * NUM_GUYS
envs        = [None] * NUM_GUYS
threads     = [None] * NUM_GUYS
rewards     = np.zeros(NUM_GUYS)
for i in range(0,NUM_GUYS):
    guys_params[i] = np.random.rand(8,111)
    envs[i]        = env = gym.make('Ant-v1')



while True:

        for i in range(0,NUM_GUYS):
            threads[i] = threading.Thread(target=run_guy, args=(guys_params[i], envs[i]))

        for i in range(0,NUM_GUYS):
            rewards[i] = threads[i].join()

        max_i = np.argmax(rewards)
        print ("Best reward:")
        print (max_i)

        guys_params[0] = guys_params[max_i]
        for i in range(1,NUM_GUYS):
            guys_params[i] = mutate(guys_params[0],rate)
