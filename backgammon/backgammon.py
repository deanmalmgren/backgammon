import random
import itertools

N_MC = 1000

def make_move(board, die):
    if board[die-1] > 0:
        board[die-1] -= 1
    else:
        # move the largest possible piece in. This fails in two scenarios:
        # 1. for doubles, it isn't maximizing all removals on turn
        # 2. it doesn't optimize chances of future rolls by spreading out blobs
        for point in range(5, die-1, -1):
            if board[point] > 0:
                board[point] -= 1
                board[point-die] += 1
                break
        else:
            for point in range(die-1, -1, -1):
                if board[point] > 0:
                    board[point] -= 1
                    break


def remove_pieces(board):
    n_pieces = sum(board)
    n_turns = 0
    # print(board)
    while sum(board) > 0:
        n_turns += 1

        # roll the dice and always have the largest number first
        dice = [random.randint(1,6), random.randint(1,6)]
        dice.sort()
        dice.reverse()
        # print(dice,)

        if dice[0] != dice[1]:
            for die in dice:
                make_move(board, die)
        else:
            die = dice[1]
            for move in range(4):
                make_move(board, die)
        # print(board)

    return n_turns


def iter_boards():
    # https://stackoverflow.com/a/28969798/564709
    n = 15
    k = 6
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]


def simulate_board(board, n_mc=N_MC, verbose=False):
    results = []
    for i in range(n_mc):
        n_turns = remove_pieces(board.copy())
        results.append(n_turns)
    if verbose:
        _results = results.copy()
        _results.sort()
        ci95_ub = int(n_mc * 0.975)
        ci95_lb = int(n_mc * 0.025)
        print(
            '{:6.3f}'.format(sum(_results)/n_mc),
            '{:2d}'.format(_results[ci95_lb]),
            '{:2d}'.format(_results[ci95_ub]),
            '||| {:2d} | {:2d} | {:2d} | {:2d} | {:2d} | {:2d}'.format(*board)
        )
    return results


def simulate_all_boards(n_mc=N_MC, verbose=True):
    for board in iter_boards():
        simulate_board(board, n_mc, verbose=verbose)


def prob_winning(board1, board2, n_mc=N_MC):
    results1 = simulate_board(board1, n_mc=n_mc)
    results2 = simulate_board(board2, n_mc=n_mc)
    n = 0
    for i in range(len(results1)):
        if results1[i] <= results2[i]:
            n += 1
    return float(n) / len(results1)


if __name__ == '__main__':
    # simulate_all_boards()
    # simulate_board([4,3,0,2,3,3], n_mc=10000, verbose=True)
    # simulate_board([0,2,1,4,4,4], n_mc=10000, verbose=True)
    p = prob_winning(
        [4,3,0,2,3,3],
        [3,2,1,4,4,1],
        n_mc=100000,
    )
    print(p)
