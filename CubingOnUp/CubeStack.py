class CubeStack(object):

    def __init__(self, cube_list):
        self.stack = cube_list


    def swap_cube(self, cube_idx_a, cube_idx_b):
        '''
        Swap a cube and index a with a cube at index b
        '''
        cube_a = self.stack[cube_idx_a]
        cube_b = self.stack[cube_idx_b]

        self.stack[cube_idx_a] = cube_b
        self.stack[cube_idx_b] = cube_a


    def validate_stack(self):
        '''
        Check if every cube on each side of the stack displays a different color
        '''
        sides = ['front', 'left', 'back', 'right']

        for side in sides:
            side_colors = [cube.data[side][0] for cube in self.stack]

            if len(side_colors) != len(set(side_colors)):
                return False

        return True


    def __str__(self):
        string = 'Cube # \t side facing top \t side facing front \n'

        for cube in self.stack:
            string = string + str(cube.data['cube_number']) + '\t\t' + cube.data['top'][1] + '\t\t\t' + cube.data['front'][1] + '\n'

        return string
