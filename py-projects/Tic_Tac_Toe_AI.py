import copy
import sys
import time

import pygame
import random
import numpy as np


# m for mode change ai to pvp

# r to restart game

# l for level changer

# from constants import *

# --- PYGAME SETUP ---


class Constants:
    def __init__(self):
        # ---------
        # CONSTANTS
        # ---------

        # --- PIXELS ---

        self.WIDTH = 600
        self.HEIGHT = 600

        self.ROWS = 3
        self.COLS = 3
        self.SQSIZE = self.WIDTH // self.COLS

        self.LINE_WIDTH = 15
        self.CIRC_WIDTH = 15
        self.CROSS_WIDTH = 20

        self.RADIUS = self.SQSIZE // 4

        self.OFFSET = 50

        # --- COLORS ---

        self.BG_COLOR = ("white")
        self.LINE_COLOR = ("black")
        self.CIRC_COLOR = (9, 231, 200)
        self.CROSS_COLOR = ("red")


const = Constants()
pygame.init()
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(const.BG_COLOR)


# --- CLASSES ---

class Board:

    def __init__(self):

        self.squares = np.zeros((const.ROWS, const.COLS))
        self.empty_sqrs = self.squares  # [squares]
        self.marked_sqrs = 0

    def final_state(self, show=False):

            # @return 0 if there is no win yet
            # @return 1 if player 1 wins
            # @return 2 if player 2 wins


        # vertical wins
        for col in range(const.COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = const.CIRC_COLOR if self.squares[0][col] == 2 else const.CROSS_COLOR
                    iPos = (col * const.SQSIZE + const.SQSIZE // 2, 20)
                    fPos = (col * const.SQSIZE + const.SQSIZE // 2, const.HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, const.LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins
        for row in range(const.ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = const.CIRC_COLOR if self.squares[row][0] == 2 else const.CROSS_COLOR
                    iPos = (20, row * const.SQSIZE + const.SQSIZE // 2)
                    fPos = (const.WIDTH - 20, row * const.SQSIZE + const.SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, const.LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = const.CIRC_COLOR if self.squares[1][1] == 2 else const.CROSS_COLOR
                iPos = (20, 20)
                fPos = (const.WIDTH - 20, const.HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, const.CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = const.CIRC_COLOR if self.squares[1][1] == 2 else const.CROSS_COLOR
                iPos = (20, const.HEIGHT - 20)
                fPos = (const.WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, const.CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(const.ROWS):
            for col in range(const.COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))

        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0


class AI:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def Level_change(self):
        if self.level:
            prev_mode = "Hard"
        else:
            prev_mode = "Easy"
        self.level = 1 if self.level == 0 else 0
        mode = "Hard" if prev_mode == "Easy" else "Easy"
        print(f"AI level changed to {mode} from {prev_mode}")
    # --- RANDOM ---

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx]  # (row, col)

    # --- MINIMAX ---

    def minimax(self, board, maximizing):

        # terminal case
        case = board.final_state()

        # player 1 wins
        if case == 1:
            return 1, None  # eval, move

        # player 2 wins
        if case == 2:
            return -1, None

        # draw
        elif board.isfull():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                    ok = 1

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                    ok = 0

            return min_eval, best_move

    # --- MAIN EVAL ---

    def eval(self, main_board):
        if self.level == 0:
            # random choice
            eval = 'random'
            move = self.rnd(main_board)
        else:
            # minimax algo choice
            eval, move = self.minimax(main_board, False)

        print(f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')

        return move  # row, col


class Game:

    def __init__(self):
        self.constant = Constants()
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1-cross  #2-circles
        self.gamemode = 'ai'  # pvp or ai
        self.running = True
        self.show_lines()

    # --- DRAW METHODS ---

    def show_lines(self):
        # bg
        screen.fill(const.BG_COLOR)

        # vertical
        pygame.draw.line(screen, const.LINE_COLOR, (const.SQSIZE, 0), (const.SQSIZE, const.HEIGHT), const.LINE_WIDTH)
        pygame.draw.line(screen, const.LINE_COLOR, (const.WIDTH - const.SQSIZE, 0),
                         (const.WIDTH - const.SQSIZE, const.HEIGHT), const.LINE_WIDTH)

        # horizontal
        pygame.draw.line(screen, const.LINE_COLOR, (0, const.SQSIZE), (const.WIDTH, const.SQSIZE), const.LINE_WIDTH)
        pygame.draw.line(screen, const.LINE_COLOR, (0, const.HEIGHT - const.SQSIZE),
                         (const.WIDTH, const.HEIGHT - const.SQSIZE), const.LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            # draw cross
            # desc line
            start_desc = (col * const.SQSIZE + const.OFFSET, row * const.SQSIZE + const.OFFSET)
            end_desc = (col * const.SQSIZE + const.SQSIZE - const.OFFSET, row * const.SQSIZE + const.SQSIZE - const.OFFSET)
            pygame.draw.line(screen, const.CROSS_COLOR, start_desc, end_desc, const.CROSS_WIDTH)
            # asc line
            start_asc = (col * const.SQSIZE + const.OFFSET, row * const.SQSIZE + const.SQSIZE - const.OFFSET)
            end_asc = (col * const.SQSIZE + const.SQSIZE - const.OFFSET, row * const.SQSIZE + const.OFFSET)
            pygame.draw.line(screen, const.CROSS_COLOR, start_asc, end_asc, const.CROSS_WIDTH)
            print(start_desc,end_desc,start_asc,end_asc)
        elif self.player == 2:
            # draw circle
            center = (col * const.SQSIZE + const.SQSIZE // 2, row * const.SQSIZE + const.SQSIZE // 2)
            pygame.draw.circle(screen, const.CIRC_COLOR, center, const.RADIUS, const.CIRC_WIDTH)

    # --- OTHER METHODS ---

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        prev_mode = self.gamemode
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'
        print(f"Game mode changed to {self.gamemode.upper()} from {prev_mode.upper()}")
    def isover(self):
        return self.board.final_state(show=True) != 0 or self.board.isfull()

    def reset(self):
        print("ENJOY THE NEW GAME")
        self.__init__()


def main():
    # --- OBJECTS ---

    game = Game()
    board = game.board
    ai = game.ai

    # --- MAINLOOP ---

    while True:

        # pygame events
        for event in pygame.event.get():

            # quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if board.isfull() or board.final_state():
                time.sleep(5)
                game.__init__()
                board = game.board
                # ai = game.ai
            # keydown event
            if event.type == pygame.KEYDOWN:

                # m - mode
                if event.key == pygame.K_m:
                    game.change_gamemode()

                # l - level changer
                if event.key == pygame.K_l:
                    ai.Level_change()

                # r - restart
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    # ai = game.ai

                # 0 - random ai
                if event.key == pygame.K_0:
                    ai.level = 0

                # 1-random ai
                if event.key == pygame.K_1:
                    ai.level = 1

            # click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // const.SQSIZE
                col = pos[0] // const.SQSIZE

                # human mark sqr
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        # AI initial call
        if game.gamemode == 'ai' and game.player == ai.player and game.running:

            # update the screen
            pygame.display.update()

            # eval
            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.isover():
                game.running = False

        pygame.display.update()


main()
