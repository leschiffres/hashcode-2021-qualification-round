# hashcode-2021-qualification-round

This is a repo containing our solution for the qualification round of google hashcode 2021. This solution allowed us to reach top 20% of the leaderboard during the competition.

To run the algorithm run in terminal: `python3 run.py`

## Brief Description

Given a city plan and all car itineraries in that city, the goal is to schedule all traffic lights, to minimize the total amount of time spent in traffic and help as many cars as possible to reach their destination. 

## Implemented Algorithms

Our solution takes into account the in & out degree of each traffic light (how many cars are passing) and assigns proportinally the time to each traffic light. Also we find out that assigning to all traffic lights 1 second of traffic time provided efficient solutions in some instances. 