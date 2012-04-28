from PySFML import sf

window = sf.RenderWindow(sf.VideoMode(640, 480),
                         "Ejemplo 01")
while True:
    window.Clear()
    window.Display()
