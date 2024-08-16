from board import Board
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

    def is_fully_expanded(self):
        pass

    def select(self):
        node = self
        while node.children != []:
            node = choice(node.children,weights=[child.value/child.visited+sqrt(log(node.visited)/(2*child.visited)) for child in node.children])
        return node
    

    def rollout(self):
        self.visited += 1
        result = self.board.random_game(self.team)
        if result == self.team:
            self.value += 1
        elif result == 0:
            self.value += .5
        return result

    def backpropagate(self,winner):
        self.visited += 1
        if self.team == winner:
            self.value += 1
        elif winner == 0:
            self.value += .5
        if self.parent:
            self.parent.backpropogate(winner)

    def expand(self):
        self.children = [McNode(move,-self.team,self) for move in self.board.legal_moves()]


class MCTS:
    def __init__(self,board,team,time):
        self.root=McNode(board,team)
        self.time=time#Set time limit

    def search(self):
        start_time = time.time()
        while time.time() - start_time < self.time_limit:
            current=self.root
            while current.children:
                current=current.select()
            if current.visited==0:
                    result=current.rollout
            else:
                current.expand()
                current=current.select()
                result=current.rollout()
            current.backpropagate(result)
        best_child = max(self.root.children, key=lambda c: c.visited)
        return best_child.board
    



        

    

