import time
import math
import random
import numpy as np
from helper import *
class Node:
    def __int__(self,state,value,visits):
        self.state=state 
        self.parent=None
        self.children=[]
        self.value=value
        # self.level=level
        self.visits=visits
class state_space:
    def __init__(self):
        self.root=None
    def add_state(self,state,value,visits):
        if self.root==None:
            head_node=Node(state,0,0)
            self.root=head_node
        else:
            new_node=Node(state,value,visits)
            parent_node.children.append(new_node)

class AIPlayer:

    def __init__(self, player_number: int, timer):
        """
        Intitialize the AIPlayer Agent

        # Parameters
        `player_number (int)`: Current player number, num==1 starts the game
        
        `timer: Timer`
            - a Timer object that can be used to fetch the remaining time for any player
            - Run `fetch_remaining_time(timer, player_number)` to fetch remaining time of a player
        """
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}: ai'.format(player_number)
        self.timer = timer

    def get_move(self, state: np.array) -> Tuple[int, int]:
        """
        Given the current state of the board, return the next move

        # Parameters
        `state: Tuple[np.array]`
            - a numpy array containing the state of the board using the following encoding:
            - the board maintains its same two dimensions
            - spaces that are unoccupied are marked as 0
            - spaces that are blocked are marked as 3
            - spaces that are occupied by player 1 have a 1 in them
            - spaces that are occupied by player 2 have a 2 in them

        # Returns
        Tuple[int, int]: action (coordinates of a board cell)
        """

        # Do the rest of your implementation here
        player=self.player_number
        tree=state_space()
        tree.add_state(state,0,1,0)
        time_remaining=fetch_remaining_time(timer, player)
        valid_actions=get_valid_actions(board)
        all_corners=get_all_corners(dim)
        all_edges=get_all_edges(dim)
        positions_on_edge=get_vertices_on_edge(edge, dim)
        position_of_corner=get_vertex_at_corner(corner, dim)
        which_edge=get_edge(pos, dim)
        which_corner=get_corner(pos, dim)
        for action in valid_actions:
            state_after_action=get_state()
            state_space.add_state(state_after_action,value,visits,parent_node=state)
            value=no of Wins 
            visits=no of visits
            
            def get_state(state,action):
                return

            def simulate_hero(self,state,action):
                
                return hero_state
            def simulate_villain(self,state,action):
                
                return villain_state
            
