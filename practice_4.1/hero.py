class Hero:
    def __init__(self, name):
        self._name = name
        self._level = 1
        self._xp = 0
        self._hp = 100

    @property
    def level(self):
        return self._level

    @property
    def xp(self):
        return self._xp

    @property
    def max_hp(self):
        return 80 + self._level * 20

    @property
    def hp(self):
        return self._hp

    @property
    def is_alive(self):
        return self._hp > 0

    def gain_xp(self, points):
        if not self.is_alive:
            raise ValueError()
        if points <= 0:
            raise ValueError()

        self._xp += points
        while True:
            required_xp = self._level * 100
            if self._xp >= required_xp:
                self._xp -= required_xp
                self._level += 1
                self._hp = self.max_hp
            else:
                break

    def take_damage(self, amount):
        if amount <= 0:
            raise ValueError()
        self._hp = max(0, self._hp - amount)

    def heal(self, amount):
        if not self.is_alive:
            raise ValueError()
        if amount <= 0:
            raise ValueError()
        self._hp = min(self.max_hp, self._hp + amount)

    def attack(self, other):
        if not isinstance(other, Hero):
            raise TypeError()
        if not self.is_alive:
            raise ValueError()
        if not other.is_alive:
            raise ValueError()
        if self is other:
            raise ValueError()

        damage = self._level * 10 + 10
        other.take_damage(damage)

        if not other.is_alive:
            xp_reward = other.level * 50
            self.gain_xp(xp_reward)

    def __repr__(self):
        return f"Hero('{self._name}', level={self._level}, xp={self._xp}, hp={self._hp}/{self.max_hp})"


arthur = Hero("Артур")
arthur.gain_xp(250)
print(arthur)

orc = Hero("Орк")
orc.take_damage(85)
print(orc.hp)

arthur.attack(orc)
print(orc.is_alive)
print(arthur)

try:
    orc.heal(10)
except ValueError:
    print("Ошибка: нельзя лечить мертвого персонажа (ValueError)")

try:
    arthur.attack(arthur)
except ValueError:
    print("Ошибка: нельзя атаковать самого себя (ValueError)")

try:
    arthur.level = 99
except AttributeError:
    print("Ошибка: нельзя изменить уровень напрямую (AttributeError)")