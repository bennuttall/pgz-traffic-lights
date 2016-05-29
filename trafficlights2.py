from gpiozero import TrafficLights

lights = TrafficLights(2, 3, 4)

WIDTH = 200
HEIGHT = 420

red = {
    'rect': Rect(50, 50, 100, 100),
    'color': (255, 0, 0),
    'led': lights.red,
}
amber = {
    'rect': Rect(50, 160, 100, 100),
    'color': (255, 194, 0),
    'led': lights.amber,
}
green = {
    'rect': Rect(50, 270, 100, 100),
    'color': (0, 255, 0),
    'led': lights.green,
}

colors = [red, amber, green]

def draw():
    screen.fill((255, 255, 255))
    for color in colors:
        screen.draw.filled_rect(color['rect'], color['color'])

def on_mouse_down(pos):
    for color in colors:
        if color['rect'].collidepoint(pos):
            color['led'].blink(n=1)
