__author__ = 'lym'


class Giraffes():
    def left_foot_forward(self):
        print('Left Foot Forward')

    def right_foot_forward(self):
        print('Right Foot Forward')

    def left_foot_backward(self):
        print('Left Foot Backward')

    def right_foot_backward(self):
        print('Right Foot Backward')

    def dance(self):
        self.left_foot_backward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.left_foot_forward()
        self.left_foot_forward()
        pass

Johny = Giraffes()
Johny.dance()
