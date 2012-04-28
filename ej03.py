from PySFML import sf

window = sf.RenderWindow(sf.VideoMode(640, 480),
                         "Ejemplo 03")
event = sf.Event()
text = sf.String("Hola Flisol")

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    window.Clear()
    window.Draw(text)
    window.Display()
