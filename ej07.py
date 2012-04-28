from PySFML import sf

class Ship(object):
    def __init__(self, x, y):
        self.image = sf.Image()
        self.image.LoadFromFile("ship.png")
        self.sprite = sf.Sprite(self.image)
        self.sprite.SetPosition(x, y)
        self.velocity = 100

    def update(self, input_, delta):
        if input_.IsKeyDown(sf.Key.Left):
            self.sprite.Move(-self.velocity * delta, 0)

        if input_.IsKeyDown(sf.Key.Right):
            self.sprite.Move(self.velocity * delta, 0)

    def draw(self, window):
        window.Draw(self.sprite)

def main():
    window = sf.RenderWindow(sf.VideoMode(640, 480),
                            "Ejemplo 07")
    window.SetFramerateLimit(60)

    ship = Ship(320, 400)
    event = sf.Event()

    running = True
    while running:
        while window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                running = False

        input_ = window.GetInput()
        ship.update(input_, window.GetFrameTime())

        window.Clear()
        ship.draw(window)
        window.Display()



if __name__ == '__main__':
    main()
