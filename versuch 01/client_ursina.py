from ursina import *
import entities
from network_ursina import NetworkManager

app = Ursina()
camera.position = (0, 20, -4)
camera.rotation = (80, 0, 0)
editor_camera = EditorCamera(enabled=False, ignore_paused=True)

start = None
ziel = None


def update():
    global start, ziel
    if not held_keys['left mouse']:
        start = None
        ziel = None


def input(key):
    global start, ziel
    if key == 'left mouse down' and mouse.hovered_entity and mouse.hovered_entity.parent == player_hand.slots:
        start = mouse.hovered_entity
    if key == 'left mouse up' and mouse.hovered_entity and mouse.hovered_entity.parent == player_area.slots:
        ziel = mouse.hovered_entity
        if start and ziel and start != ziel:
            start.parent = ziel.parent
            start.x = ziel.x
            print(start.name)
            print(start.typ)
            print(start.x)
            n.send_data(start)
            start = None
            ziel = None

    if key == 'tab':
        editor_camera.enabled = not editor_camera.enabled

    if key == 's':
        camera.rotation_x += 1

    if key == 'w':
        camera.rotation_x -= 1

    if key == 'p':
        print(camera.position)
        print(camera.rotation)

    if key == 'c':
        player_hand.append_card()

    if key == 'b':
        player_hand.clear_hand()


n = NetworkManager()
n.position = (-.6, .4)
n.scale = .5
board = entities.Board()
player_area = entities.PlayerArea()
enemy_area = entities.EnemyArea()
player_hand = entities.PlayerHand()

app.run()
