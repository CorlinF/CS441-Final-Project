
from random import choice
from math import sqrt, log
import time

class McNode:
    def __init__(self,board,team,parent=None):
        self.board=board
        self.team=team
        self.parent=parent
        self.children=[]
        self.visited=0
        self.value=0

    def select(self):
        node = self
        while node.children != []:
            node = choice(node.children,weights=[child.value//child.visited+sqrt(log(node.visited)/(2*child.visited)) for child in node.children])
        return node
    
    def rollout(self,num_rollout):
        total_value=0
        self.visited += 1
        for _ in range(num_rollout):
            result = self.board.random_game(self.team)
            if result == self.team:
                total_value += 1
            elif result == 0:
                total_value += .5
        self.value=total_value/num_rollout
        return self.value
    
    def backpropagate(self, value):
        self.visited += 1
        self.value += value 
        if self.parent:
            self.parent.backpropagate(value)
        
    def expand(self):
        legal_moves = self.board.legal_moves()
        if not legal_moves:
            print("No legal moves available.")
        self.children = [McNode(move, -self.team, self) for move in legal_moves]


class MCTS:
    def __init__(self,board,team,time):
        self.root=McNode(board,team)
        self.time=time#Set time limit

    def search(self,times=10):
        start_time = time.time()
        while time.time() - start_time < self.time:
            current=self.root
            while current.children:
                current=current.select()
            if current.visited==0:
                average_value = current.rollout(times)
                current.backpropagate(average_value)
            else:
                current.expand()
                current = current.select()
                average_value = current.rollout(times)
                current.backpropagate(average_value)
        best_child = max(self.root.children, key=lambda c: c.visited)
        return best_child.board
    



        

    

