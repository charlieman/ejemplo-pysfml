from PySFML import sf

class Sprite(object):
    def __init__(self, image, x, y):
        self.image = sf.Image()
        self.image.LoadFromFile(image)
        self.sprite = sf.Sprite(self.image)
        self.sprite.SetPosition(x, y)

    def draw(self, window):
        window.Draw(self.sprite)

class Ship(Sprite):
    def __init__(self, x, y):
        super(Ship, self).__init__("ship.png", x, y)
        self.velocity = 150

    def update(self, input_, delta):
        if input_.IsKeyDown(sf.Key.Left):
            self.sprite.Move(-self.velocity * delta, 0)

        if input_.IsKeyDown(sf.Key.Right):
            self.sprite.Move(self.velocity * delta, 0)


class Invader(Sprite):
    def __init__(self, x, y):
        super(Invader, self).__init__("alien.png", x, y)
        self.x_velocity = 100
        self.y_velocity = 10
        self.going_right = True
        self.going_down = False
        self.initial_x = x
        self.y_distance = 0
        self.sprite.SetColor(sf.Color.Green)
        self.count = 0

    def update(self, delta):
        x_pos, y_pos = self.sprite.GetPosition()
        x, y = 0, 0

        if not self.going_down:
            if x_pos > self.initial_x + 50 or \
            x_pos < self.initial_x - 50:
                self.going_right = not self.going_right
                self.count = (self.count +1) % 5

        x = self.x_velocity * (self.going_right * 2 -1) * delta

        if self.count == 4:
            self.going_down = True

        if self.going_down:
            y = self.y_velocity * delta
            self.y_distance += y
            if self.y_distance > 3:
                self.going_down = False
                self.y_distance = 0

        self.sprite.Move(x, y)

def main():
    window = sf.RenderWindow(sf.VideoMode(640, 480),
                            "Ejemplo 08")
    window.SetFramerateLimit(60)

    ship = Ship(320, 400)
    aliens = []
    for i in range(8):
        for j in range(4):
            aliens.append(Invader(100 + i * 50, 30 + j * 50))

    event = sf.Event()
    running = True
    while running:
        while window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                running = False

        input_ = window.GetInput()
        delta = window.GetFrameTime()
        ship.update(input_, delta)
        for alien in aliens:
            alien.update(delta)

        window.Clear()
        ship.draw(window)
        for alien in aliens:
            alien.draw(window)
        window.Display()



if __name__ == '__main__':
    main()
