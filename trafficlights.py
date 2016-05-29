from gpiozero import TrafficLights

lights = TrafficLights(2, 3, 4)

WIDTH = 200
HEIGHT = 420

red = Rect(50, 50, 100, 100)
amber = Rect(50, 160, 100, 100)
green = Rect(50, 270, 100, 100)

def draw():
    screen.fill((255, 255, 255))
    screen.draw.filled_rect(red, (255, 0, 0))
    screen.draw.filled_rect(amber, (255, 194, 0))
    screen.draw.filled_rect(green, (0, 255, 0))

def on_mouse_down(pos):
    if green.collidepoint(pos):
        lights.green.blink(n=1)
    if amber.collidepoint(pos):
        lights.amber.blink(n=1)
    if red.collidepoint(pos):
        lights.red.blink(n=1)
