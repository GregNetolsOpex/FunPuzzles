import Cube
import CubeStack
import random

cube_1 = {'cube_number': 1,
          'front': ('red','b'),
          'back': ('green','d'),
          'left': ('red','a'),
          'right': ('red','f'),
          'top': ('blue','e'),
          'bottom': ('yellow','c')}

cube_2 = {'cube_number': 2,
          'front': ('red','b'),
          'back': ('blue','d'),
          'left': ('red','a'),
          'right': ('yellow','f'),
          'top': ('green','e'),
          'bottom': ('yellow','c')}

cube_3 = {'cube_number': 3,
          'front': ('blue','b'),
          'back': ('red','d'),
          'left': ('green','a'),
          'right': ('green','f'),
          'top': ('yellow','e'),
          'bottom': ('blue','c')}

cube_4 = {'cube_number': 4,
          'front': ('green','b'),
          'back': ('red','d'),
          'left': ('blue','a'),
          'right': ('yellow','f'),
          'top': ('green','e'),
          'bottom': ('yellow','c')}

def CubingOnUp():
    cube_1_obj = Cube.Cube(cube_1)
    cube_2_obj = Cube.Cube(cube_2)
    cube_3_obj = Cube.Cube(cube_3)
    cube_4_obj = Cube.Cube(cube_4)

    cube_list = [cube_1_obj, cube_2_obj, cube_3_obj, cube_4_obj]
    cube_stack = CubeStack.CubeStack(cube_list)

    print(cube_stack.validate_stack())
    print(cube_stack)

    '''
    Randomly pick a Cube from the CubeStack
    Either rotate it left or clockwise
    Check if it is a valid stack
    '''
    counter = 0
    #while( not cube_stack.validate_stack() and counter < 1000000 ):
    while( counter < 10000000 ):
        counter = counter + 1
        if counter % 100000 == 0:
            print(counter)

        idx = random.randint(0, len(cube_stack.stack)-1)

        if random.getrandbits(1):
            cube_stack.stack[idx].rotate_left()
        else:
            cube_stack.stack[idx].rotate_clockwise()

        if cube_stack.validate_stack():
            print(cube_stack.validate_stack())
            print(cube_stack)

if __name__ == "__main__":
    CubingOnUp()
