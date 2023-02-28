---
layout: single
title: "Introduction to Reinforcement Learning (Part 03: Q-Learning in Python)"
header:
  image: "https://live.staticflickr.com/65535/51227976855_8d59f8284f_w.jpg"
  teaser: "https://live.staticflickr.com/65535/51227976855_8d59f8284f_w.jpg"
categories:
  - reinforcement-learning
tags:
  - Reinforcement-learning
  - Tutorial
  - Intelligent Agent
  - Artificial Intelligence
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---

Q-learning is a value-based Reinforcement learning where Q-values are used to determine action in a particular state. The Q-values are updated iteratively and the maximum Q-value defines the action-policy at each state.





### Q-value or Action-value
Q-values is the action-state value and the goal is to maximize the $Q(s,a)$

$$U(s) = \max_a Q(s,a)$$

Now, action/exploration may be required to discover the environment and thus learn the $Q(s,a)$

At each iteration, the Q-value is updated as follows:

$$Q(s,a) \leftarrow r(s,a) + \gamma \cdot max_{a^\prime} Q(s^\prime, a^\prime)$$

here,
* $r(s,a) \leftarrow$ immediate reward
* $\gamma \leftarrow$ discount factor
* $s^\prime \leftarrow$ next state after taking action $a$

Now, after a number of iteration, the selected action is

$$\pi(s) = {\arg\max}_a Q(s,a)$$


The algorithm looks like:

> while True:
> 	- select an action $a$
> 	- receive the immediate reward, $r$
> 	- observe new state $s^\prime$
> 	- update $Q(s,a) = r(s,a) + \gamma \cdot max_{a^\prime} Q(s^\prime, a^\prime)$


 ### Temporal-Difference Learning
 Now, to learn from the environment, an agent will follow:

$$Q^{new}(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha \cdot \Big ( r_t + \gamma \cdot max_a Q(s_{t+1},a) -Q(s_t,a_t) \Big)$$

You may have seen the same equation in a different form in a paper as follow:s
$$Q^{new}(s_t,a_t) \leftarrow \alpha \cdot \Big ( r_t + \gamma \cdot max_a Q(s_{t+1},a) \Big) + (1-\alpha) \cdot Q(s_t,a_t)$$

where
* $\alpha \in (0,1] \rightarrow$ learning rate
* $(1-\alpha) \cdot Q(s_t,a_t) \rightarrow$ current Q-value weighted by learning rate
* $\alpha \cdot r_t = \alpha \cdot r(s_t,a_t) \rightarrow$ reward for action $a_t$ taken at state $s_t$
* $\gamma \in (0,1]$ discount factor for future rewards

also, a few terminologies of `temporal difference` (TD Learning) to keep in mind,
* TD target $\leftarrow r_t + \gamma \cdot max_a Q(s_{t+1},a)$ 
* TD Delta $\leftarrow$ TD target $-$ Q(s_t,a_t) 
* $Q^{new}(s_t,a_t) \leftarrow Q(s_t,a_t) + \alpha \cdot$ TD Delta

### Choosing Action based on $\epsilon-$`greedy` policy
The policy refers to choosing aactions using the current Q-value estimates
* $1-\epsilon$ proability to choose action that has the highest Q-value
* $\epsilon$ probability to choose a random action

### $\epsilon-$`decay`
Exploration is important only when the agent starts interacting with the environment. Over time, the agent perceives more information about the environment and need to focus more on exploitation. $\epsilon \approx 0$ results in greater exploitation and less exploration. That's why we will gradually move towards zero for the $\epsilon$. This is called $\epsilon-$decay.

## Q-learning Algorithm in Python
### Environment
In this post, we will not cover how to build an environment in python. We will look at just some basics of what functions are available from an environment.

If you want to use `OpenAI gym` environments, you can simply create an object of the environment. For example,

* `FrozenLake` game
	```python
	import gym
	env = gym.make("FrozenLake-v0")
	```
* `CartPole` game
	```python
	import gym
	env = gym.make('CartPole-v0')
	```
Now, we can check the length of `observation space` and `action space` as follows
```python
state_space_size = env.observation_space.n
action_space_size = env.action_space.n
```

Note that, if the `state_space_size` and `action_space_size` are small in number, we can use simple `Q-learning` algorithm. If the size of state and action spaces are large, we should use `DQN` aka Deep Q-Network. I will cover `DQN` in a later post.


### Training Q-agent
```python
import numpy as np
import random

# define the initial Q-table (all zeroes)
q_table = np.zeros([state_space_size, action_space_size])

# Hyperparameters
episodes = 1000
alpha = 0.1
gamma = 0.6
epsilon = 0.1

# storing information for graph
reward_per_episode = []

for _ in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
	    # epsilon-greedy algorithm for selecting action
	    # exploration
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        # exploitation
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done, info = env.step(action)
        
        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

		# calculate total reward
		total_reward += reward
	
	# epsilon decay (could vary, just example)
	epsilon = DECAY_EPSILON(epsilon)
	
	# append total reward per episode to the list	
	reward_per_episode.append(total_reward)
```

here, the `DECAY_EPSILON()` function can vary based on the coder. A simple decay could be as follows:
```python
MIN_EPSILON = 0.0
def DECAY_EPSILON(epsilon, episode, MIN_EPSILON):
	delta = (epsilon - MIN_EPSILON)/episode
	epsilon = epsilon - delta
	return epsilon
```

or define the rate and then do the following
```python
DECAY_RATE = 0.0005
def DECAY_EPSILON(epsilon, DECAY_RATE):
	epsilon = epsilon * (1 - DECAY_RATE)
	return epsilon
```

### Evaluating Q-Agent
The testing agent does not need the `exploration`, therefore, requiring only the exploitation at each state.
```python
# Hyperparameters
episodes = 100

for _ in range(episodes):
    state = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        action = np.argmax(q_table[state])
        next_state, reward, done, info = env.step(action) 
        
        # calculate total reward
		total_reward += reward

	# append total reward per episode to the list	
	reward_per_episode.append(total_reward)
```

Now, we can check whether we are getting the expected rewards per episode.


## References
1. [Geeks for Geeks: Q-Learning in Python](https://www.geeksforgeeks.org/q-learning-in-python/)
2. [Wikipedia: Q-learning](https://en.wikipedia.org/wiki/Q-learning)
3. [Reinforcement Q-Learning from Scratch in Python with OpenAI Gym](https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/)
4. [DEEPLIZARD: Reinforcement Learning - Goal Oriented Intelligence](https://deeplizard.com/learn/video/HGeI30uATws)
5. [Reward Based Epsilon Decay](https://aakash94.github.io/Reward-Based-Epsilon-Decay/)
6. [Q – Learning Algorithm with Step by Step Implementation using Python](https://www.analyticsvidhya.com/blog/2021/04/q-learning-algorithm-with-step-by-step-implementation-using-python/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ2MzMwNDYzOF19
-->