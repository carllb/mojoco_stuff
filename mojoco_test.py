import gym
import numpy as np
import qcartpole_template

env = gym.make('Ant-v1')
observation = env.reset()
reward = 0
done = False

policy = np.random.rand(8,111)

best = None
best_policy = policy

a = 0.1
b = 0.9

it = 0.0

while True:
        total_reward = 0
        policy = a * best_policy + a * np.random.rand(8,111)
        observation = env.reset()
        for i in range(1,100 + int(it)):
                #env.render()
                action = policy * observation
                observation, reward, done, info = env.step(action) # take a random action
                total_reward += reward
                if done:
                        break
        if best == None:
                best = total_reward
                best_policy = policy
        elif total_reward > best:
                best = total_reward
                best_policy = policy
        #print (total_reward)
        print (best)
        a += 0.00001
        b = 1 - a
        it+= 0.01
        if a > 0.9999:
                print ("Best total reward:")
                print (best)
                break
