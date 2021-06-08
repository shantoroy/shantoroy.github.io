---
layout: single
title: "Introduction to Reinforcement Learning (Part 01: Basic Concepts)"
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



Reinforcement learning (RL) has been quite a popular field in both academia and industries as it helps to build intelligent agents and can solve automation-based problems.

In this tutorial, we will step towards the very basic concepts of RL. I plan to continue the tutorial as a series where we will learn more about theories and implementation of different algorithms in `Python`. So, stay tuned.

## Reinforcement Learning (RL)
RL defines the learning process of an intelligent agent that perceives environment states, learns to choose an action in that state that leads to the maximum cumulative reward at the end of a game.
<figure>
  <a href="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"><img src="https://live.staticflickr.com/65535/51226516036_e486b2a319_w.jpg"></a>
</figure>

In python, it is like:
```python
obs = env.reset()
done = False
while not done:
	action = agent.get_action(obs)
	next_obs, reward, done, info = env.step(action)
	obs = next_obs
```


## Reinforcement Learning Terminologies
### Basic Terminologies


- **Environment**  – is a typical physical world (could be a game or game-alike problems) where an agent or player learns to choose particular actions at each state of the game. Example: A Chess game. 

	`Markov Decision Process (MDP)` is typically used to define an environemt. A MDP is represented as a 4-tuple ($S,A,P_a,R_a$), where $S$ is a set of states, $A$ is a set of actions, $P_a \big( s, s^{\prime} \big) = Pr \big( s_{t+1} = s^{\prime} \vert s_t = s, a_t = a \big)$  is the probability of reaching to state $s^{\prime}$ if an action $a$ is taken at state $s$, and $R_a \big( s, s^{\prime} \big)$ is the immediate reward.



- **Agent**  – is a learner whose target is to maximize the cumulative reward at each time step of a game. The agent finds a policy to understand the best action to take given a particular state of the environment. Example: each player in a Chess game  is defined as the agent whose target is to win the game with best possible combination of moves.

- **Action ($a$)**  – a list of actions that an agent can perform at each state of the environment. Example: At the beginning state of Chess, a player can use any of his pawns to go forward, or any of the Knights.

- **State ($s$)**  – the present condition of the agent/player in the environment. Example: The beginning condition of a Chess board where a player is yet to take an action.

- **Reward ($r$)**  – for each action taken by an agent, the environment outputs a reward. It’s usually a scalar value and nothing but feedback from the environment

### Additional Important Terminologies
- **Discount Factor ($\gamma$)** - In a RL problem, the agent tries to maximize the cumulative reward at each time step $t$,

	$total\ reward = \sum_{k=0}^T R_{t+k+1}$
	
	However, not all rewards are equally important, for example the distant future rewards. In that case, we discount the future rewards by multiplying the rewards with a discount factor  $\gamma \in [0,1)$. Therefore, our cumulative expected (discounted) rewards is
	
	$total\ reward = \sum_{k=0}^\infty \big[\gamma^k \cdot R_{t+k+1} \big]$
	$= R_{t+1} + \gamma \cdot R_{t+2} + \gamma^2 \cdot R_{t+3} \dots$	
	
- **Policy ($\pi$)**  – defines the action strategy at a particular state (the current state). For a deterministic policy, the action to take at a particular state is the policy. If Stochastic, it outputs a probability of an action. We will see more details later. It can be stochastic, $a_t \sim \pi(\centerdot \vert s_t)$ or deterministic, $a_t = \pi(s_t)$

-   **Value ($V$)** - The expected long-term return with discount, as opposed to the short-term reward  $R$.  Here,  the $V_\pi(s)$, is defined as the expected long-term return of the current state  $s$  under policy  $\pi$.


-   **Q-value or Action-value ($Q$)** - Q-value is similar to the Value Function, except that it takes an extra parameter, the current action  $a$. Here, the Q-value function, $Q_\pi(s, a)$  refers to the long-term return of the current state  $s$, taking action  $a$  under policy  $\pi$.

- **Trajectory (sometimes called as Episodes, $\tau$)** - A sequence of state, action, and rewards, e.g., $\tau \rightarrow (s_2, a_2, r_3,s_3,a_3,r_4,s_4)$ that influence those environment states
	- The initial state $s_0$ is sampled over initial distribution $\mu$
	$$s_0 \sim \mu(\centerdot)$$ 
	- deterministic state transition, $s_{t+1} = f(s_t,a_t)$
	- stochastic state transition, $s_{t+1} \sim Pr(\centerdot \vert s_t,a_t)$

## Final Objective of RL
Our target is to make the agent learn the best policy ($\pi^*$) that maximizes the expected cumulative reward

$$\pi^* = \arg \max_\pi E_{\tau \sim \pi} \big[ R(\tau) \big]$$

where, $\tau \sim \pi$ means
- $s_0 \sim \mu(\centerdot)$
- $a_t \sim \pi(\centerdot \vert s_t)$
- $s_{t+1} \sim Pr(\centerdot \vert s_t,a_t)$

## How RL works
Based on the objectives, RL takes different approcahes to solve a particular problem. Here, we will get introduced to the primary approaches to solve RL problems.

-   **Value-based Approach** - in this approach, an agent tries to maximize a value function  $V(s)$, which  is the value of the cumulative reward which an agent expects to gain in the future.  
      
	  $$V_\pi(s) = E_\pi \big[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + ...|S_t = s \big]$$
    
    
  
  
-   **Policy-based** - in a policy-based RL approach, an agent tries to build a policy that outputs the optimal action performed at each state to gain maximum reward in the future. Here, the policy  $π$  determines the next action  $a$  at any state  $s$ and can be represented as $a = \pi(s)$. There are two types of policy-based RL methods -
    
    -   **Deterministic** - at the current state  $s$, the policy  $π$ outputs the action $a$ to take.

    -   **Stochastic** - each action has a certain probability, given by the equation below -
      
	    $$\pi (a|s) = Pr \big(A_t=a|S_t=s \big)$$

- **Model-based** - this approach requires an additional model of the environment.

## Temporal Difference Learning
TD-learning is a type of model-free reinforcement learning method (not model-based) by performing random-sampling of the current state of the value function.

$V(S_t) \leftarrow V(S_t) + \alpha \big[ R_{t+1} +\gamma \cdot V(S_{t+1}) - V(S_t) \big]$

Here,
- $V(S_t) \rightarrow$ is the previous estimate
- $\alpha \rightarrow$ learning rate
- $R_{t+1} \rightarrow$ reward at the next state
- $\gamma \cdot V(S_{t+1}) \rightarrow$ discounted value at the next step
- $R_{t+1} + \gamma \cdot V(S_{t+1}) \rightarrow$ TD Target

## Workflow
- Problem Formulation and Model Buildup
- Create an Environment based on model
- Define Actions and Observations for the agent(s)
- Define the Reward function of the agent(s)
- Create the agent(s)
- Train and validate the agent(s)
- Deploy the policy (policies in multi-agent games)


## Reading/Watch Lists and Resources
- [Awesome Reinforcement Learning](https://github.com/aikorea/awesome-rl)
- [Awesome Deep Reinforcement Learning](https://github.com/brianspiering/awesome-deep-rl)
- [Course in Deep Reinforcement Learning](https://github.com/andri27-ts/Reinforcement-Learning#week-2---rl-basics-mdp-dynamic-programming-and-model-free-control)
- [Deep RL Bootcamp](https://sites.google.com/view/deep-rl-bootcamp/lectures)
- [Coursera - Practical Reinforcement Learning](https://www.coursera.org/learn/practical-rl?specialization=aml)
- [Udacity - Reinforcement Learning](https://www.udacity.com/course/reinforcement-learning--ud600)

## Applications

- Industrial Robot Automation
-  Video Games
- Self Driving Cars
- Drone Shipping
- Bots
- Cyber Security

In the next tutorial, we will learn some additional concepts and other glossaries that will strengthen our base to learn about RL.

## References
* [Introduction to Reinforcement Learning for Beginners-Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/02/introduction-to-reinforcement-learning-for-beginners/)
* [Introduction to Reinforcement Learning-Datacamp](https://www.datacamp.com/community/tutorials/introduction-reinforcement-learning)
* [Introduction to Reinforcement Learning- Joshua Achiam](https://github.com/jachiam/rl-intro/blob/master/Presentation/rl_intro.pdf)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2ODI0MjAyMjgsLTE1MDI1NjE2MjYsMT
k3NDY0MTMyNSwtMjQzMjIzNDQ0LC0xNTczMzIyNjAwLDE2NDQw
OTM5ODIsNTE0Nzc4OTc1LDE3MjE4ODE4MjIsLTcxMTE4MTU2MS
wtMTkyNTc4NzE1Myw2OTQ1MzU0MTUsMTY4MjM3OTIyMSwxNjk5
NjUyNTM3LDY5ODEzODk0NiwtMTk2NzY3MTgxOCw2OTgxMzg5ND
YsLTY1MTc4NDkzMCw0MjgxMDg2NDgsLTMwNjMxNjA3NSwtNTc1
NTcwMDUxXX0=
-->