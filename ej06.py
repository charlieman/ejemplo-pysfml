from PySFML import sf

window = sf.RenderWindow(sf.VideoMode(640, 480),
                         "Ejemplo 06")
window.SetFramerateLimit(60)

ship_image = sf.Image()
ship_image.LoadFromFile("ship.png")
ship = sf.Sprite(ship_image)
ship.SetPosition(320, 400)
velocity = 100
event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    inpt = window.GetInput()
    if inpt.IsKeyDown(sf.Key.Left):
        ship.Move(-velocity * window.GetFrameTime(), 0)
    if inpt.IsKeyDown(sf.Key.Right):
        ship.Move(velocity * window.GetFrameTime(), 0)

    window.Clear()
    window.Draw(ship)
    window.Display()
