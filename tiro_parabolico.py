from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Mueve los elementos y mantiene la animación activa."""
    # Asegura que haya un objetivo desde el inicio.
    if not targets or randrange(40) == 0:
        targets.append(vector(199, randrange(-150, 150)))

    for target in targets:
        target.x -= 2

        # Los objetivos que salen reaparecen por la derecha.
        if not inside(target):
            target.x = 199
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Elimina objetivos alcanzados por un disparo activo.
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if not inside(ball) or abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Programa siempre el siguiente movimiento.
    ontimer(move, 30)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
