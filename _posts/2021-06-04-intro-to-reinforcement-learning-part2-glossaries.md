---
layout: single
title: "Introduction to Reinforcement Learning (Part 02: Glossaries)"
header:
  image: "https://live.staticflickr.com/65535/52718364503_44032e3ab3_o.png"
  teaser: "https://live.staticflickr.com/65535/52718364503_44032e3ab3_o.png"
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


In the [previous post](https://shantoroy.com/reinforcement-learning/intro-to-reinforcement-learning-part1-basic-concepts/), we have learned the very basic concepts of Reinforcement Learning. In this post, we will go through different terminologies that are required to know to go further.

### Agent and Environment
An entity that interacts with the environment and takes particular actions to obtain maximum or optimal rewards. In the physical world, a Robot is a proper axample. Suppose, a robot serves as a waiter in a restaurant; the surrounding, food section, corridor, and customers are the robot's environment; and movements are actions.


### State and State Space
In RL, a state represents the current situation or environment in which the agent is operating. It is a way to capture all the relevant information that the agent needs to make decisions.

State space is typically the set of all possible states an environment may have in a predefined condition. 
    
### Action and Action Space
An action is a choice made by the agent in response to a given state. It is the decision that the agent takes based on its current observation.

Action space is typically the set of actions an agent can perform to interact with the environment. For example, for a vacuum cleaner, it might be move forward, left, right, back, and break.
    
### Reward
A reward is a feedback signal that the agent receives after taking an action. It is a way to provide feedback to the agent whether its taken actions were good or bad. 

### Episode
The entire path of states and taken actions to reach the goal constitutes one of the many episodes. Usually, the agent learn through reaching the goal over and over again by exploring different actions on the way.  
    
### Policy
A policy is a strategy that the agent uses to decide which actions to take in different states. It is a way to map states to actions.
    
### Value
The value of a state is the expected long-term reward that an agent can receive starting from that state. It is a way to evaluate the goodness of a state.
    
### Q-value
A Q-value is the expected long-term reward that an agent can receive by taking a specific action in a given state. It is a way to evaluate the goodness of an action. In the next tutorial, we will learn more about Q-learning.
    
### Exploration vs. Exploitation
The trade-off between exploration and exploitation is a critical concept in RL. Exploration refers to the agent's desire to explore new states and actions to learn more about the environment. Exploitation refers to the agent's desire to take actions that have led to good rewards in the past (based on experience).

### Discount Factor
The discount factor is a number between 0 and 1. It is used to update the policy by discounting rewards. A future reward in N steps forward is usually multiplied by the discount factor to define the rewards' importance to the agent.

### Policy Gradient
A policy gradient is a technique used to optimize a policy in RL. It involves taking the gradient of the policy with respect to the reward and updating the policy parameters accordingly.
    
### Monte Carlo Methods
Monte Carlo methods are a family of techniques used to estimate the value of a state or action based on random sampling of the environment.

    
### Temporal Difference Learning
Temporal difference (TD) learning is a technique used to learn the value of a state or action based on the difference between the predicted value and the actual reward received.


So, these are some of the basic terminology we should know to learn more about reinforcement learning. In the next tutorial, we will learn, [how to code Q-learning in Python](https://shantoroy.com/reinforcement-learning/intro-to-reinforcement-learning-part3-RL-types/).

That's all for today! See you in the next post!!! :sunglasses:
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgzMTU2ODExMSwtMTM0MzY1ODE4MV19
-->