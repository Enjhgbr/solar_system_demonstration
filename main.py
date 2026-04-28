import pygame as pg
import math



SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pg.display.set_mode(size)
PLANET_ORBIT_RADIUS = 150
PLANET_RADIUS = 15
SUN_RADIUS = 100

FPS = 40

clock = pg.time.Clock()



class Planets:
    def __init__(self, color, orbit_radius, radius, speed):
        self.color = color
        self.orbit_radius = orbit_radius
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def update(self):
        self.angle += self.speed





    def draw(self):
        x = SCREEN_WIDTH / 2 + self.orbit_radius * math.cos(math.radians(self.angle))

        y = SCREEN_HEIGHT / 2 + self.orbit_radius * math.sin(math.radians(self.angle))

        pg.draw.circle(screen, pg.Color(self.color), (x, y), self.radius)

        pg.draw.circle(screen, pg.Color("yellow"), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 40)














mercury = Planets("orange", PLANET_ORBIT_RADIUS * 0.4, PLANET_RADIUS * 0.5, 1)
venus = Planets("brown", PLANET_ORBIT_RADIUS *  0.7, PLANET_RADIUS * 0.8, 0.8)
earth = Planets("green", PLANET_ORBIT_RADIUS, PLANET_RADIUS, 0.5)
mars = Planets("red", PLANET_ORBIT_RADIUS * 1.5, PLANET_RADIUS * 0.6, 0.2)
jupiter = Planets("gray", PLANET_ORBIT_RADIUS * 2, PLANET_RADIUS * 2.2, 0.1)
saturn = Planets("#ffff96", PLANET_ORBIT_RADIUS * 2.7, PLANET_RADIUS * 1.9, 0.07)
uranus = Planets("blue", PLANET_ORBIT_RADIUS * 3.5, PLANET_RADIUS * 1.6, 0.05)
neptune = Planets("pink", PLANET_ORBIT_RADIUS * 4.2, PLANET_RADIUS * 1.3, 0.03)
solar_system = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


while True:
    screen.fill(pg.Color("black"))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    for planet in solar_system:
        planet.draw()
        planet.update()

    pg.display.flip()
    clock.tick(FPS)
