from ursina import *


class PlayerHand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture='white_cube',
            texture_scale=(7, 1),
            color=color.clear,
            scale=(.7, .15, 0)*2,
            origin=(0, -.5),
            position=(0, -.5, 0)
        )
        self.slots = Entity(parent=self, scale=((1/7, 1)))

    def append_card(self):
        if len(self.slots.children) > 6:
            print('hand voll')
            return
        else:
            card = Card(parent=self.slots, x=self.free_slot())

    def free_slot(self):
        slot_list = [-3, -2, -1, 0, 1, 2, 3]
        if len(self.slots.children) == 0:
            print('keine Karte vorhanden')
            return -3
        for c in self.slots.children:
            if c.x in slot_list:
                slot_list.remove(int(c.x))
        return slot_list[0]

    def hand_size(self):
        if len(self.slots.children) == 0:
            return 1
        else:
            return len(self.slots.children)

    def destroy_card(self, x):
        for c in self.slots.children:
            if c.x == x:
                destroy(c)

    def clear_hand(self):
        for c in self.slots.children:
            destroy(c)


class PlayerArea(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='quad',
            texture='white_cube',
            texture_scale=(7, 1),
            color=color.orange,
            highlight_color=color.yellow,
            position=(0, .105, -1),
            rotation_x=90,
            scale=(7, 1.5, 1))

        self.slots = Entity(parent=self, scale=((1 / 7, 1)))
        for s in range(-3, 4):
            slot = Button(parent=self.slots,
                          origin=(0, 0),
                          position=(s, 0, -.01))


class EnemyArea(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='quad',
            texture='white_cube',
            texture_scale=(7, 1),
            color=color.white,
            position=(0, .105, 1),
            scale=(7, 1.5, 1),
            rotation=(90, 180, 0))


class Card(Button):
    def __init__(self, parent, x):
        super().__init__(
            model='cube',
            texture='white_cube',
            origin=(0, -.5),
            color=color.blue,
            highlight_scale = 1.2
        )
        self.name = None
        self.parent = parent
        self.x = x
