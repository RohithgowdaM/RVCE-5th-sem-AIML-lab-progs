# 2 different approaches
# <--First approach-->
hooray="hooorrrayyy"


def print_state(state):
    for row in state:
        print(" ".join(map(str, row)))


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move_up(state):
    i, j = find_blank(state)
    if i > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
        return new_state
    else:
        return None


def move_down(state):
    i, j = find_blank(state)
    if i < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
        return new_state
    else:
        return None


def move_left(state):
    i, j = find_blank(state)
    if j > 0:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
        return new_state
    else:
        return None


def move_right(state):
    i, j = find_blank(state)
    if j < 2:
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
        return new_state
    else:
        return None


def calculate_heuristic(state, goal_state):
    # Simple heuristic: count the number of misplaced tiles
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h


def a_star(initial_state, goal_state):
    OPEN = [(calculate_heuristic(initial_state, goal_state), 0, initial_state)]
    CLOSED = set()

    while OPEN:
        f, g, current_state = min(OPEN)
        OPEN.remove((f, g, current_state))
        CLOSED.add(tuple(map(tuple, current_state)))

        print_state(current_state)
        print(" ")

        if current_state == goal_state:
            print(f"{hooray}Solution found!")
            return

        successors = [
            (move_up(current_state), "UP"),
            (move_down(current_state), "DOWN"),
            (move_left(current_state), "LEFT"),
            (move_right(current_state), "RIGHT")
        ]

        successors = [(s, move) for s, move in successors if s is not None and tuple(
            map(tuple, s)) not in CLOSED]

        for successor, move in successors:
            h = calculate_heuristic(successor, goal_state)
            g_successor = g + 1
            f_successor = g_successor + h

            if (h, g_successor, successor) not in OPEN:
                OPEN.append((f_successor, g_successor, successor))

    print(f"{hooray}No solution found.")


# Updated example usage with the provided input
initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [2, 8, 1],
    [0, 4, 3],
    [7, 6, 5]
]

a_star(initial_state, goal_state)





#<--Second approach-->
# class Node:
#     def __init__(self,data,level,fval):
#         """ Initialize the node with the data, level of the node and the calculated fvalue """
#         self.data = data
#         self.level = level
#         self.fval = fval

#     def generate_child(self):
#         """ Generate child nodes from the given node by moving the blank space
#             either in the four directions {up,down,left,right} """
#         x,y = self.find(self.data,'_')
#         """ val_list contains position values for moving the blank space in either of
#             the 4 directions [up,down,left,right] respectively. """
#         val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
#         children = []
#         for i in val_list:
#             child = self.shuffle(self.data,x,y,i[0],i[1])
#             if child is not None:
#                 child_node = Node(child,self.level+1,0)
#                 children.append(child_node)
#         return children
       
#     def shuffle(self,puz,x1,y1,x2,y2):
#         """ Move the blank space in the given direction and if the position value are out
#             of limits the return None """
#         if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
#             temp_puz = []
#             temp_puz = self.copy(puz)
#             temp = temp_puz[x2][y2]
#             temp_puz[x2][y2] = temp_puz[x1][y1]
#             temp_puz[x1][y1] = temp
#             return temp_puz
#         else:
#             return None
           

#     def copy(self,root):
#         """ Copy function to create a similar matrix of the given node"""
#         temp = []
#         for i in root:
#             t = []
#             for j in i:
#                 t.append(j)
#             temp.append(t)
#         return temp    
           
#     def find(self,puz,x):
#         """ Specifically used to find the position of the blank space """
#         for i in range(0,len(self.data)):
#             for j in range(0,len(self.data)):
#                 if puz[i][j] == x:
#                     return i,j


# class Puzzle:
#     def __init__(self,size):
#         """ Initialize the puzzle size by the specified size,open and closed lists to empty """
#         self.n = size
#         self.open = []
#         self.closed = []

#     def accept(self):
#         """ Accepts the puzzle from the user """
#         puz = []
#         for i in range(0,self.n):
#             temp = input().split(" ")
#             puz.append(temp)
#         return puz

#     def f(self,start,goal):
#         """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
#         return self.h(start.data,goal)+start.level

#     def h(self,start,goal):
#         """ Calculates the different between the given puzzles """
#         temp = 0
#         for i in range(0,self.n):
#             for j in range(0,self.n):
#                 if start[i][j] != goal[i][j] and start[i][j] != '_':
#                     temp += 1
#         return temp
       

#     def process(self):
#         """ Accept Start and Goal Puzzle state"""
#         print("Enter the start state matrix \n")
#         start = self.accept()
#         print("Enter the goal state matrix \n")        
#         goal = self.accept()

#         start = Node(start,0,0)
#         start.fval = self.f(start,goal)
#         """ Put the start node in the open list"""
#         self.open.append(start)
#         print("\n\n")
#         while True:
#             cur = self.open[0]
#             print("")
#             print("  | ")
#             print("  | ")
#             print(" \\\'/ \n")
#             for i in cur.data:
#                 for j in i:
#                     print(j,end=" ")
#                 print("")
#             """ If the difference between current and goal node is 0 we have reached the goal node"""
#             if(self.h(cur.data,goal) == 0):
#                 break
#             for i in cur.generate_child():
#                 i.fval = self.f(i,goal)
#                 self.open.append(i)
#             self.closed.append(cur)
#             del self.open[0]

#             """ sort the opne list based on f value """
#             self.open.sort(key = lambda x:x.fval,reverse=False)


# puz = Puzzle(3)
# puz.process()