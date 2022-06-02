from ursina import *


class Board(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='table2',
            scale=(10, 0.2, 6)
        )


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
            position=(0, -.4, 0)
        )

        self.slots = Entity(parent=self, scale=(1/7, 1))

    def append_card(self):
        if len(self.slots.children) > 6:
            return
        else:
            card = Card(parent=self.slots, x=self.free_slot())

    def free_slot(self):
        slot_list = [-3, -2, -1, 0, 1, 2, 3]
        if len(self.slots.children) == 0:
            return -3
        for c in self.slots.children:
            if c.x in slot_list:
                slot_list.remove(int(c.x))
        return slot_list[0]

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
            origin=(0, 0),
            rotation=(90, 0, 0),
            scale=(7, 1.5, 1)
        )

        self.slots = Entity(parent=self, scale=(1 / 7, 1))
        for s in range(-3, 4):
            slot = Button(parent=self.slots,
                          origin=(0, 0),
                          position=(s, 0, -.01)
                          )


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
            rotation=(90, 180, 0)
        )


class Card(Button):
    def __init__(self, parent, x):
        super().__init__(
            model='cube',
            scale=(1, 1, .03),
            texture='white_cube',
            origin=(0, 0),
            color=color.blue
        )

        self.typ = None
        self.name = None
        self.parent = parent
        self.x = x

    def highlight(self):
        if mouse.hovered_entity == self:
            self.color = color.pink
            self.scale = (1.2, 1.2, .03)
            self.z = -.3
        else:
            self.color = color.blue
            self.scale = (1, 1, .03)
            self.z = -.2

    def update(self):
        self.highlight()
