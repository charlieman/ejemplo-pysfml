# Include the PySFML extension
from PySFML import sf

# Create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "Ejemplo 03")

# Create a graphical string to display
text = sf.String("Hello SFML")

event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    window.Clear()
    window.Draw(text)
    window.Display()
