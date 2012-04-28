from PySFML import sf
from random import random

class Sprite(object):
    def __init__(self, image, x, y):
        self.image = sf.Image()
        self.image.LoadFromFile(image)
        self.sprite = sf.Sprite(self.image)
        self.width, self.height = self.sprite.GetSize()
        self.sprite.SetCenter(self.width/2, self.height/2)
        self.sprite.SetPosition(x, y)
        self.dead = False

    def get_rect(self):
        x, y = self.sprite.GetPosition()
        return sf.FloatRect(x - self.width/2,
                            y - self.height/2,
                            x + self.width/2,
                            y + self.height/2)

    def draw(self, window):
        window.Draw(self.sprite)

    def die(self):
        self.dead = True

class Ship(Sprite):
    def __init__(self, x, y):
        super(Ship, self).__init__("ship.png", x, y)
        self.velocity = 150
        self.score = 0
        self.bullet_rest = sf.Clock()

    def update(self, input_, delta):
        if input_.IsKeyDown(sf.Key.Left):
            self.sprite.Move(-self.velocity * delta, 0)

        if input_.IsKeyDown(sf.Key.Right):
            self.sprite.Move(self.velocity * delta, 0)

    def score_up(self, points):
        self.score += points

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
        self.bullet_rest = sf.Clock()

    def update(self, ship, delta):
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

        if self.get_rect().Intersects(ship.get_rect()):
            ship.die()
            self.die()

class Bullet(Sprite):
    def __init__(self, ship, up=True):
        x, y = ship.sprite.GetPosition()
        super(Bullet, self).__init__("bullet.png", x, y)
        self.up = up
        self.velocity = -300 if up else 200

    def update(self, aliens, ship, delta):
        self.sprite.Move(0, self.velocity * delta)
        rect = self.get_rect()
        if self.up:
            for alien in aliens:
                if rect.Intersects(alien.get_rect()):
                    alien.die()
                    self.die()
                    ship.score_up(10)
        else:
            if rect.Intersects(ship.get_rect()):
                ship.die()
                self.die()

def main():
    window = sf.RenderWindow(sf.VideoMode(640, 480),
                            "Ejemplo 08")
    window.SetFramerateLimit(60)

    score = sf.String("Score: ")
    score.SetSize(30)
    score.SetPosition(5, 5)

    ship = Ship(320, 400)
    aliens = []
    bullets = []
    for i in range(8):
        for j in range(4):
            aliens.append(Invader(100 + i * 50, 30 + j * 50))

    event = sf.Event()
    running = True
    while running:
        while window.GetEvent(event):
            if event.Type == sf.Event.Closed:
                running = False
            elif event.Type == sf.Event.KeyPressed and \
               event.Key.Code == sf.Key.Space:
                if ship.bullet_rest.GetElapsedTime() > 0.5:
                    bullets.append(Bullet(ship))
                    ship.bullet_rest.Reset()

        input_ = window.GetInput()
        delta = window.GetFrameTime()
        ship.update(input_, delta)

        for alien in aliens:
            alien.update(ship, delta)
            if alien.bullet_rest.GetElapsedTime() > 5 and \
                random() < 0.001:
                bullets.append(Bullet(alien, False))
        aliens = filter(lambda x: not x.dead, aliens)

        for bullet in bullets:
            bullet.update(aliens, ship, delta)
        bullets = filter(lambda x: not x.dead, bullets)

        if not aliens:
            print "Ganaste!"
            print "Tu puntaje es de: %s" % ship.score
            running = False

        if ship.dead:
            print "Fin del juego"
            print "Tu puntaje es de: %s" % ship.score
            running = False

        score.SetText("Score: %d" % ship.score)

        window.Clear()
        ship.draw(window)
        for alien in aliens:
            alien.draw(window)
        for bullet in bullets:
            bullet.draw(window)
        window.Draw(score)
        window.Display()

if __name__ == '__main__':
    main()
