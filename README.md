# Ticket to Ride random route generator

The goal of this project is to genereate new routes for Ticket to Ride Europe.  This project was presented at PyLadiesCon 2025 as *Ticket To Ride + Python: Coding the ultimate expansion pack with a random route generator*.  The talk is on <a href="https://www.youtube.com/watch?v=RKgj9YFlERQ">YouTube</a>.

## Motivation
Our family enjoys playing board games and my 9-year old kid loves beating me.  He consistently wins in the game Ticket to Ride.  He knows all of the routes in the Europe version so he can block me as soon as I start building routes.  In an effort to finally win, I wrote a random route generator in Python.  

## Overview
We explored coding the random route generator through the lens of computational thinking.
We decomposed a large problem into a smaller one, abstracted our train routes as a graph, used algorithmic thinking to calculate the shortest route using n calculating the shortest path, and then testing and iteration. 

The random route generator was developed in several parts.
1. Choose any two cities at random.
2. Decomposition: Calculated the shortest distance on a smaller map.
3. Algorithmic thinking: used Dijkstra's algorithm to compute the shortest distance.  
4. Abstraction: Represented our graph of cities as a matrix and then a dictionary. 
5. Testing and iteration - we played the game and made code changes.

## Code
There are two versions of this code.  We developed our code in `ticket_to_ride_generator.ipynb` and also wrote `ticket_to_ride_generator.py` to be a text-based game in the terminal.
