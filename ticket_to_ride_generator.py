# This code generates random routes for the game Ticket to Ride Europe.
# This is the companion code the PyLadiesCon 2025 talk
# Ticket to Ride + Python: Coding the ultimate expansion pack with a random route generator
# This was written as a script to have a text-based game version.

import random
from collections import defaultdict
import heapq
import os

train_routes = {
    'Lisboa': [('Cadiz', 2), ('Madrid', 3)],
    'Cadiz': [('Lisboa', 2), ('Madrid', 3)],
    'Madrid': [('Lisboa', 3), ('Cadiz', 3), ('Barcelona', 2), ('Pamplona', 3)],
    'Barcelona': [('Madrid', 2), ('Pamplona', 2), ('Marseille', 4)],
    'Pamplona': [('Madrid', 3), ('Barcelona', 2), ('Paris', 4), ('Marseille', 4), ('Brest', 4)],
    'Marseille': [('Barcelona', 4), ('Paris', 4), ('Zürich', 2), ('Roma', 4), ('Pamplona', 4)],
    'Paris': [('Pamplona', 4), ('Marseille', 4), ('Zürich', 3), ('Bruxelles', 2), ('Dieppe', 1), ('Frankfurt', 3), ('Brest', 3)],
    'Bruxelles': [('Paris', 2), ('Dieppe', 2), ('Amsterdam', 1), ('Frankfurt', 2)],
    'Dieppe': [('Paris', 1), ('Bruxelles', 2), ('London', 2), ('Brest', 3)],
    'London': [('Dieppe', 2), ('Edinburgh', 4), ('Amsterdam', 2)],
    'Edinburgh': [('London', 4)],
    'Amsterdam': [('Bruxelles', 1), ('Essen', 3), ('Frankfurt', 2), ('London', 2)],
    'Essen': [('Amsterdam', 3), ('Frankfurt', 2), ('Berlin', 2), ('København', 3)],
    'Frankfurt': [('Essen', 2), ('Bruxelles', 2), ('München', 2), ('Paris', 3), ('Berlin', 4), ('Amsterdam', 2)],
    'München': [('Frankfurt', 2), ('Zürich', 2), ('Wien', 3), ('Venezia', 2)],
    'Zürich': [('München', 2), ('Marseille', 2), ('Paris', 3), ('Venezia', 2)],
    'Venezia': [('München', 2), ('Roma', 2), ('Zagreb', 2), ('Zürich', 2)],
    'Roma': [('Venezia', 2), ('Marseille', 4), ('Palermo', 4), ('Brindisi', 2)],
    'Palermo': [('Roma', 4), ('Brindisi', 3), ('Smyrna', 6)],
    'Brindisi': [('Palermo', 3), ('Roma', 2), ('Athina', 4)],
    'Athina': [('Brindisi', 4), ('Sofia', 3), ('Smyrna', 2), ('Sarajevo', 4)],
    'Smyrna': [('Athina', 2), ('Palermo', 6), ('Constantinople', 2), ('Angora', 3)],
    'Constantinople': [('Smyrna', 2), ('Sofia', 3), ('Sevastopol', 4), ('Angora', 2), ('Bucuresti', 3)],
    'Sofia': [('Athina', 3), ('Constantinople', 3), ('Bucuresti', 2), ('Sarajevo', 2)],
    'Sarajevo': [('Sofia', 2), ('Zagreb', 3), ('Athina', 4), ('Budapest', 3)],
    'Zagreb': [('Sarajevo', 3), ('Venezia', 2), ('Budapest', 2), ('Wien', 2)],
    'Budapest': [('Zagreb', 2), ('Wien', 1), ('Bucuresti', 4), ('Kyiv', 6), ('Sarajevo', 2)],
    'Wien': [('München', 3), ('Budapest', 1), ('Zagreb', 2), ('Warszawa', 4)],
    'Bucuresti': [('Budapest', 4), ('Sofia', 2), ('Sevastopol', 4), ('Kyiv', 4), ('Constantinople', 4)],
    'Sevastopol': [('Bucuresti', 4), ('Constantinople', 4), ('Rostov', 4), ('Sochi', 2), ('Erzurum', 3)],
    'Rostov': [('Sevastopol', 4), ('Sochi', 2), ('Kharkov', 2)],
    'Kharkov': [('Rostov', 2), ('Kyiv', 4), ('Moskva', 4)],
    'Kyiv': [('Budapest', 6), ('Bucuresti', 4), ('Warszawa', 4), ('Smolensk', 3), ('Wilno', 2), ('Kharkov', 4)],
    'Wilno': [('Kyiv', 2), ('Warszawa', 3), ('Smolensk', 3), ('Riga', 4), ('Petrograd', 4)],
    'Warszawa': [('Wilno', 3), ('Kyiv', 4), ('Danzig', 2), ('Berlin', 4), ('Wien', 4)],
    'Berlin': [('Warszawa', 4), ('Essen', 2), ('Danzig', 4), ('Wien', 3), ('Frankfurt', 2)],
    'Danzig': [('Berlin', 4), ('Warszawa', 2), ('Riga', 3)],
    'Riga': [('Danzig', 3), ('Wilno', 4), ('Petrograd', 4)],
    'Petrograd': [('Riga', 4), ('Moskva', 4), ('Wilno', 2), ('Stockholm', 8)],
    'Moskva': [('Petrograd', 4), ('Smolensk', 2), ('Kharkov', 4)],
    'Smolensk': [('Moskva', 2), ('Wilno', 3), ('Kyiv', 3)],
    'Sochi': [('Rostov', 2), ('Erzurum', 3), ('Sevastopol', 4)],
    'Erzurum': [('Sochi', 3), ('Angora', 3), ('Sevastopol', 4)],
    'København': [('Essen', 3), ('Stockholm', 3)],
    'Stockholm': [('København', 3), ('Petrograd', 8)],
    'Angora': [('Smyrna', 3), ('Constantinople', 2), ('Erzurum', 3)],
    'Brest': [('Paris',3), ('Pamplona', 4), ('Dieppe', 2)],
}

locations = list(train_routes.keys())

def clear_output():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def dijkstra(train_routes, start_city: str):
    shortest_routes = defaultdict(lambda: float('inf'))
    shortest_routes[start_city] = 0

    visited = set()
    queue = [(0, start_city)]

    while queue:
        current_min_distance, current_city = heapq.heappop(queue)
        visited.add(current_city)

        for neighbor, distance in train_routes[current_city]:
            if neighbor not in visited:
                shortest_routes[neighbor] = min(distance + current_min_distance, shortest_routes[neighbor])
                heapq.heappush(queue, [distance + current_min_distance, neighbor])

    return shortest_routes


def draw_route_card(map_list):
    # Draw two cities and return the city names and the shortest distance given a map

    # Pick two cities
    city1, city2 = random.sample(map_list, 2)

    # Get shorest distances from city1 to all cities
    small_map_shortest = dijkstra(train_routes, city1)

    # Return shortest distance from city1 to city2
    return (city1, city2, small_map_shortest[city2])

def draw_cards(name, stage):
    # Draw cards for the start or for a later draw.  Keeps track of player cards and discarded cards.
    # Input str name: player name
    # Input str stage: 'start' or 'draw'
    # Output

    player_hand = dict()
    drawn_routes = dict()
    discard_routes = dict()

    if stage == 'start':
        num_cards = 4
        num_keep = 2

    elif stage == 'draw':
        num_cards = 3
        num_keep = 1

    print(f"{name}, please draw {num_cards} route cards and keep at least {num_keep}. \n")
    print("Here are your choices: ")

    for i in range(0, num_cards):
        city1, city2, distance = draw_route_card(locations)
        route_name = f"{city1}-{city2}"

        drawn_routes[route_name] = distance
        print(f"[{i + 1}] {city1} to {city2}, distance {distance}.")

    for route in drawn_routes:
        picked = False

        while not picked:
            keep = input(f"Keep {route}? (y or n) ")

            if keep == 'y' or keep == 'Y' or keep == 'yes' or keep == 'Yes':
                player_hand[route] = drawn_routes[route]
                picked = True

            elif keep == 'n' or keep == 'N' or keep == 'no' or keep == 'No':
                discard_routes[route] = drawn_routes[route]
                picked = True

            else:
                print('Please enter "y" or "n".')
                picked = False

    print("\nDrawn routes: ")
    print(drawn_routes)

    print(f"\n{name}'s routes: ")
    print(player_hand)

    print("\nDiscarded routes: ")
    print(discard_routes)

    print(f"\n{name}, your turn is finished. \n")

    return (player_hand, discard_routes)


def play_game():
    # Draws cards, keeps track of player hands and discarded routes
    # Writes actions to a log file

    print("Welcome to Ticket to Ride - the Python expansion pack!")

    log_file = 'ticket_to_ride_log.txt'
    all_discard_routes = []
    name1 = input("Input the name for Player 1: ")

    player1_hand, discard1 = draw_cards(name1, 'start')
    all_discard_routes.append(discard1)

    with open(log_file, "a") as file:
        file.write("Begin the game!\n")
        file.write(f"Player 1: {name1}\n")
        file.write(f"{name1}'s routes: {str(player1_hand)}\n")
        file.write(f"Discarded routes: {str(discard1)}\n")

    print("Ready for the next player!")
    keystroke = input("Press enter for hide results.")
    clear_output()

    name2 = input("Input the name for player 2: ")

    player2_hand, discard2 = draw_cards(name2, 'start')
    all_discard_routes.append(discard2)
    with open(log_file, "a") as file:
        file.write(f"Player 2: {name2}\n")
        file.write(f"{name2}'s routes: {str(player2_hand)}\n")
        file.write(f"Discarded routes: {str(discard2)}\n")

    keystroke = input("Press enter to hide results.")
    clear_output()

    end_game = False

    while not end_game:
        print("Next options... players can view routes or draw more routes... or end the game.")
        end_game_text = input("Continue (c) or end the game (e)? ")

        if end_game_text == 'e':
            end_game = True
            clear_output()
            break
        elif end_game_text not in ('c', 'e'):
            print("Please enter 'c' to continue or 'e' to end.")
            continue

        player_num = input(f"Which player? [1] {name1} or [2] {name2} (Enter 1 or 2): ")

        if player_num == '1':
            player_name = name1
            player_hand = player1_hand
        elif player_num == '2':
            player_name = name2
            player_hand = player2_hand

        action = input("Which action? View (v) or draw (d)? ")

        if action == 'd':
            print(f"{player_name} will now draw routes.")
            new_routes, new_discard_routes = draw_cards(player_name, 'draw')
            all_discard_routes.append(new_discard_routes)

            if player_num == '1':
                player1_hand.update(new_routes)
            elif player_num == '2':
                player2_hand.update(new_routes)

            keystroke = input("Press enter to hide results.")
            clear_output()

        elif action == 'v':
            print(f"{player_name} will now view routes.")
            print(player_hand)

            keystroke = input("Press enter to hide results.")
            clear_output()

    print("End of the game!\n")

    with open(log_file, "a") as file:
        file.write("=" * 20)
        file.write("\nEnd of the game!\n")

    player1_total = sum(list(player1_hand.values()))

    print(f"{name1}'s hand: ")
    print(player1_hand, '\n')
    print(f"If you finished all of your routes, your score is {player1_total}")

    with open(log_file, "a") as file:
        file.write(f"{name1}'s hand: ")
        file.write(f"{str(player1_hand)}\n")
        file.write(f"If you finished all of your routes, your score is {player1_total}\n\n")

    player2_total = sum(list(player2_hand.values()))
    print(f"{name2}'s hand: ")
    print(player2_hand)
    print(f"If you finished all of your routes, your score is {player2_total}\n")

    with open(log_file, "a") as file:
        file.write(f"Player 2: {name2}")
        file.write(f"{name2}'s routes: {str(player2_hand)}\n")
        file.write(f"If you finished all of your routes, your score is {player2_total}\n\n")

    print('Discarded routes:')
    print(all_discard_routes)

    with open(log_file, "a") as file:
        file.write(f"Discarded routes: {str(all_discard_routes)}\n\n")

    print(f"\nThank you for playng Ticket to Ride - the Python expansion pack!")


play_game()