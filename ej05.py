from PySFML import sf

window = sf.RenderWindow(sf.VideoMode(640, 480),
                         "Ejemplo 05")
window.SetFramerateLimit(60)
text = sf.String("M")
text.SetSize(50)
rect = text.GetRect()
text.SetCenter(rect.GetWidth()/2, rect.GetHeight()/2)
text.SetRotation(180)
text.SetPosition(320, 400)
velocity = 100 #pixeles por segundo
event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    inpt = window.GetInput()
    if inpt.IsKeyDown(sf.Key.Left):
        text.Move(-velocity * window.GetFrameTime(), 0)
    if inpt.IsKeyDown(sf.Key.Right):
        text.Move(velocity * window.GetFrameTime(), 0)

    window.Clear()
    window.Draw(text)
    window.Display()
