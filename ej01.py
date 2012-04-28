# Include the PySFML extension
from PySFML import sf

# Create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "Ejemplo 01")

while True:
    window.Clear()
    window.Display()
