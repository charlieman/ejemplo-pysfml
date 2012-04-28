# Include the PySFML extension
from PySFML import sf

# Create the main window
window = sf.RenderWindow(sf.VideoMode(640, 480), "Ejemplo 04")

text = sf.String("M")
text.SetSize(30)
rect = text.GetRect()
text.SetCenter(rect.GetWidth()/2, rect.GetHeight()/2)
text.SetRotation(180)
text.SetPosition(320, 400)

textrotation = 180
event = sf.Event()

running = True
while running:
    while window.GetEvent(event):
        if event.Type == sf.Event.Closed:
            running = False
        elif event.Type == sf.Event.KeyPressed:
            if event.Key.Code == sf.Key.Left:
                textrotation += 3
            if event.Key.Code == sf.Key.Right:
                textrotation -= 3
            if event.Key.Code == sf.Key.Z:
                text.Move(-5, 0)
            if event.Key.Code == sf.Key.X:
                text.Move(5, 0)

    textrotation = textrotation % 360
    text.SetRotation(textrotation)

    window.Clear()
    window.Draw(text)
    window.Display()
