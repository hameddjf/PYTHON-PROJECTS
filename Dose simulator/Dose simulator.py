import pygame
from pygame.locals import *
pygame.init()

SCREEN_SIZE = (450, 450)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class TicTacToe:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.current_player = 'X'
        self.font = pygame.font.SysFont(None, 100)

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                x = j * 150
                y = i * 150
                pygame.draw.rect(self.screen, WHITE, (x, y, 150, 150), 2)
                text_surface = self.font.render(self.board[i][j], True, BLACK)
                text_position = text_surface.get_rect(center=(x+75, y+75))
                self.screen.blit(text_surface, text_position)

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def get_click_position(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row = y // 150
                    col = x // 150
                    if self.board[row][col] == '':
                        return row, col

    def check_for_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False

    def run(self):
        while True:
            self.screen.fill(BLUE)
            self.draw_board()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    row, col = self.get_click_position()
                    self.board[row][col] = self.current_player
                    if self.check_for_winner():
                        print(self.current_player + ' wins!')
                        pygame.quit()
                        sys.exit()
                    self.switch_player()
            pygame.display.update()

if __name__ == '__main__':
    game = TicTacToe()
    game.run()