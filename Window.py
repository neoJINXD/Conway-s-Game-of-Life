import pyglet
from game import gameOfLife
from pyglet.window import mouse


class myWindow(pyglet.window.Window):

    def __init__(self):
        super().__init__(800, 800)
        self.game = gameOfLife(self.get_size()[0], self.get_size()[1], 10)
        pyglet.clock.schedule_interval(self.update, 1.0 / 24.0)

    def update(self, dt):

        self.game.update()

    def on_draw(self):
        self.clear()
        self.game.draw()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        print('(%s , %s)' % (x, y))

    def on_mouse_enter(self, x, y):
        print('AN INVASION!!')

    def on_mouse_leave(self, x, y):
        print('theyre gone, fiouf')


if __name__ == "__main__":
    win = myWindow()
    pyglet.app.run()
