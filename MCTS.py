from board import Board
from random import choice
from math import sqrt, log

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
    def __init__(self,board,time):
        self.root=board
        self.time=time#Set time limit

    def search():
        pass

    

