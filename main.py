#function builtin
import os
import time
import itertools
#function local
import eviroment

new_eviroment = eviroment.eviroment

####################################
#           pacman_config          #
####################################
class Pacman:
    '''object pacman
    default: pattern Sigleton
    '''

    def __init__(self,
                 live: int,
                 position_X: int,
                 position_Y: int
        ) -> None:
        self.live: int = live
        self.position_X: int = position_X
        self.position_Y: int = position_Y

    def move_pacman(self, move: str) -> None:
        """"""
        if move == 'up':
            self.position_Y -= 1
        elif move == 'rigth':
            self.position_X += 1
        elif move == 'down':
            self.position_Y += 1
        elif move == 'lefth':
            self.position_X -= 1

    def get_position_xy(self) -> list[int, int]:
        """"""
        return [
                self.position_Y,
                self.position_X,
        ]
####################################
#     event_eviroment_config       #
####################################
class EventEviroment:
    ''''''
    def __init__(self,
                 eviroment: list,
                 pacman
        ):
        self.pacman = pacman
        self.eviroment = eviroment

    def set_position_pacman_in_eviroment(self) -> None:
        """"""
        set_move = self.pacman.get_position_xy()
        new_eviroment[set_move[0]][set_move[1]] = 3


####################################
#         eviroment_config         #
####################################
class RenderEviroment:
    '''object Eviroment
    default: method target
    '''

    def __init__(self, eviroment: list) -> None:
        self.eviroment = eviroment

    def render_style_eviroment(self) -> list[str]:
        """fuction fro show array with style"""
        counter = 0
        for i in list(itertools.chain(*self.eviroment)):
            counter += 1
            # caracter background color set in terminal
            if i == 1:
                print(f'\033[41m   \033[;m', end='')
            elif i == 2:
                print('\033[33;40m • \033[;m', end='')
            elif i == 3:
                print('\033[33;40m ✪ \033[;m', end='')
            elif i == 0:
                print('\033[40m   \033[;m', end='')
            # junp line columns equal 21
            if counter == 21:
                counter = 0
                print('')
        

def color() -> None:
    """show all color"""
    for i in range(0,100,1):
        print(f'\033[{i};40mcasa\033[;m',i)
    


lives = 5
test_position_x = 10
test_position_y = 10

if __name__ == '__main__':

    pacman = Pacman(
            lives,
            test_position_x,
            test_position_y
            )
    event_eviroment = EventEviroment(
            new_eviroment,
            pacman
            )
    render_eviroment = RenderEviroment(
            new_eviroment
            )
    while True:
        os.system('clear')
        event_eviroment.set_position_pacman_in_eviroment()
        render_eviroment.render_style_eviroment()
        pacman.move_pacman('up')

        time.sleep(1)

        os.system('scrot')


























































































































