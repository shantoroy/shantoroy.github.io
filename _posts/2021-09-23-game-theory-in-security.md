---
layout: single
title: "A Comprehensive Overview of Game Theory in Cyber Security"
header:
  image: "https://live.staticflickr.com/65535/51647825732_3f23aa12a4_b.jpg"
  teaser: "https://live.staticflickr.com/65535/51647825732_3f23aa12a4_b.jpg"
categories:
  - Security
tags:
  - Game Theory
  - Security
  - Cyber Security
  - Security Games
  - Nash Equilibrium
  - Stackelberg Game
toc: true
toc_label: "Table of Contents"
toc_icon: "heart"
---


Game theory is the study of strategic decision making using mathematical model, which has recently attracted security researchers to develop strategies for the defender. It is like solving an environmental problem by solving an equation.

Lloyd Shapley, John von Neumann, John Forbes Nash Jr., and many other mathematicians made significant contribution to the fundamentals of the game theory. By the way, there is a movie named "[A Beautiful Mind (2001)](https://en.wikipedia.org/wiki/A_Beautiful_Mind_(film))" on the life of John Nash.

## Basic
Games are develped based on a particular environment and the it has four basic elements

### Players
Players can be anyone who interact with each other. In security games, we consider two players: the attacker and the defender.
 
### Actions
Each player has a set of actions and in each move, a player takes an action. For example, in a recent [paper](https://arxiv.org/pdf/2109.07724.pdf) of ours, we considered the attacker's action is to compromise a device or not. In contrast, the defender's action is to set attestation probabilities for each device. We always assume that that each player knows the possible actions of the opponents.

### Payoff
The received reward of each player given an action or strategy. It might have positive or negative values.

### Strategies
Plan of actions that determines which action to take in each move against the opponent. It may require the knowledge of own or opponenet's action history.


## Types of Games
### Cooperative vs. Non-cooperative
In cooperative games, players can plan together or make binding agreements before playing the game. In contrast, in non-cooperative games, each player determines his own strategy; there is no binding or agreement. 

### Symmetric vs. Asymmetric
In Symmetric games, the payoffs (rewards) depend on the player's  strategy. Here, strategies adoped by all players are same. Example symmetric game is `prisoner’s dilemma` In contrast, the received payoffs depend on the player in an asymmetric game. Here, strategies adoped by all players are different. Security games are good examples of asymmetric games where defender and attacker have different strategies.

### Zero-sum vs. Non-zero-sum 
In zero-sum games, the gain of a player is equal to the loss of the oppenent. For example, if $G_A$ is the attacker $A$'s gain and $L_D$ is the defender $D$'s loss, it can be presented as $G_A = -L_D$. In non-zero or general-sum games, the sum of outcomes of all players is not zero and can be anything given the strategies and reward structures. If the sum remains constant independent of whatever strategies chosen by the players, the game is called a constant-sum game.

### Static vs. Dynamic Games
Static games are played only once at the same time given each player's strategy. We often use the term `one-shot security game` when we create a static game defining a security environment and calculate payoffs of the attacker and the defender after just one round. In dynamic or repeated games, players move repeatedly and we often define the whole process using `Markov Decision Process (MDP)`. Stochastic games are repeated games with probabilistic transitions between the previous and next states. Payoffs of players depend on the current state and chosen actions.

### Simultaneous vs. Sequential
In simultaneous games, the players can take action simultaneously, i.e., at the same time step without observing other players' choices. In contrast, the players can observe or have knowledge about the previous actions taken by other players and there is a specific order for the players to give a move. In most security games, we consider sequential games where the attacker and the defender take actions one after another and have knowledge of the past events.

### Perfect vs. Imperfect Information
In an imperfect information game, the players do not know when an opponent makes a move. In contrast, in a perfect information game, the players know all the actions taken by the other players.

### Complete vs. Incomplete Information
In an incomplete information game, the payers do not know opponents strategies or payoffs. In contarst, in a complete information game, the players know the strategies, preferences, and payoffs of the other players.

### Deterministic vs. Non-deterministic
In deterministic games, the output is known given a certain action. In non-deterministic games, there might be different outputs given a player's action, i.e., something entirely different things can happen given a particular action. 


## Game Modeling
### Nash Game
Nash equilibrium provides solution of a `non-cooperative game` involving two or more players. Here, each player knows the best strategies of other players that lead to the equilibrium. However, none of them can gain more than the received payoff by changing only their own strategies.

### Stackelberg Games
Stackelberg Security Game (SSG) is a leader-follower model where the leader (defender) acts first and then the follower (attacker) chooses the best response. SSG has recently been deployed for determining security strategies in the airports, transportation, shipping, poaching, and many other application areas.

### Stackelberg vs. Nash in Security Games
In Nash games, players can change strategies at any point. However, in Stackelberg games, the leader always acts first and the reward of the leader is always greater than the followers. That means, in a SSG, the defender's payoff is always greater than the payoff received by the attacker while playing the best response.


## Example Environments in Security
1. Cyber Deception
2. Moving Target Defense
3. Intrusion Detection System
4. IoT Remote Attestation
5. Smart Grid
6. Packet Forwarding
7. Denial-of-service (DoS)
8. Cryptography and Steganography
9. Sensor Networks
10. Security of Physical and MAC layer


## References
1. [Game theory in network security](https://www.slideshare.net/RahmaSallam/game-theory-in-network-security)
2. [Game theory and security](https://www.slideserve.com/mariel/game-theory-and-security)
3. [An introduction to Game Theory](https://www.slideshare.net/paultraf/an-introduction-to-game-theory)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzQ2MzA3OTldfQ==
-->