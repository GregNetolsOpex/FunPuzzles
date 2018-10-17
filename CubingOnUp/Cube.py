class Cube(object):

    def __init__(self, data):
        '''
        param: data dictionary with the keys:
            cube_number: number label for a cube
            front:  tuple- (color, side)
            back:   tuple- (color, side)
            left:   tuple- (color, side)
            right:  tuple- (color, side)
            top:    tuple- (color, side)
            bottom: tuple- (color, side)
        '''
        self.data = data


    def rotate_left(self):
        '''
        Rotates the cube to the left as if you are viewing it from the front
        '''
        current_front   = self.data['front']
        current_back    = self.data['back']
        current_left    = self.data['left']
        current_right   = self.data['right']

        self.data['front']    = current_right
        self.data['back']     = current_left
        self.data['left']     = current_front
        self.data['right']    = current_back


    def rotate_clockwise(self):
        '''
        Rotates the cube clockwise as it you are viewing it from the front
        '''
        current_top     = self.data['top']
        current_right   = self.data['right']
        current_bottom  = self.data['bottom']
        current_left    = self.data['left']

        self.data['top']      = current_left
        self.data['right']    = current_top
        self.data['bottom']   = current_right
        self.data['left']     = current_bottom
