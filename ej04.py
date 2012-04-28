from PySFML import sf

window = sf.RenderWindow(sf.VideoMode(640, 480),
                         "Ejemplo 04")

text = sf.String("Hola Flisol")
text.SetSize(50)
rect = text.GetRect()
text.SetCenter(rect.GetWidth()/2, rect.GetHeight()/2)
text.SetPosition(320, 240)
event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
        elif event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Left:
                text.Move(-5, 0)
            if event.Key.Code == sf.Key.Right:
                text.Move(5, 0)

    window.Clear()
    window.Draw(text)
    window.Display()
