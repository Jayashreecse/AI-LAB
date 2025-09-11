from collections import deque

# Goal state for quick checking
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible moves with blank (0) position index shifts
MOVES = {
    'UP': -3,
    'DOWN': 3,
    'LEFT': -1,
    'RIGHT': 1
}

def get_blank_pos(state):
    return state.index(0)

def is_valid_move(blank_pos, move):
    # Validate left move: blank can't be in leftmost column
    if move == 'LEFT' and blank_pos % 3 == 0:
        return False
    # Validate right move: blank can't be in rightmost column
    if move == 'RIGHT' and blank_pos % 3 == 2:
        return False
    # Validate up move: blank can't be in top row
    if move == 'UP' and blank_pos < 3:
        return False
    # Validate down move: blank can't be in bottom row
    if move == 'DOWN' and blank_pos > 5:
        return False
    return True

def move_blank(state, move):
    blank_pos = get_blank_pos(state)
    if not is_valid_move(blank_pos, move):
        return None  # Invalid move

    new_blank_pos = blank_pos + MOVES[move]
    state_list = list(state)
    # Swap blank and target tile
    state_list[blank_pos], state_list[new_blank_pos] = state_list[new_blank_pos], state_list[blank_pos]
    return tuple(state_list)

def dls(state, goal, limit, visited, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    visited.add(state)

    for move in MOVES:
        new_state = move_blank(state, move)
        if new_state and new_state not in visited:
            result = dls(new_state, goal, limit - 1, visited, path + [new_state])
            if result is not None:
                return result

    return None

def iddfs(start, goal, max_depth=20):
    for depth in range(max_depth):
        visited = set()
        print(f"Trying depth limit: {depth}")
        path = dls(start, goal, depth, visited, [start])
        if path is not None:
            return path
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

if __name__ == "__main__":
    # Initial state example:
    start_state = (1, 2, 3,
               5, 6, 4,
               7, 8, 0)

    print("Start State:")
    print_board(start_state)

    solution = iddfs(start_state, GOAL_STATE)

    if solution:
        print(f"Solution found in {len(solution) -1} moves:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found within depth limit.")
