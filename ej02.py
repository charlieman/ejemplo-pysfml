# Include the PySFML extension
from PySFML import sf

# Create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "Ejemplo 02")

event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False

    window.Clear()
    window.Display()
