# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 09

from random import randint


class Entity:
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, hp, atk):
        self.__name = name
        self.__hp = hp
        self.__atk = atk

    # Lengkapi getter dan setter
    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.__hp = new_hp

    # TODO: Lengkapi method-method dibawah ini
    def attack(self, other):
        damage = self.get_atk()
        other.take_damage(damage)

    def take_damage(self, damage):
        current_hp = self.get_hp()
        self.set_hp(current_hp - damage)

    def is_alive(self):
        return self.__hp > 0

    def __str__(self):
        # Akan digunakan untuk print nama
        return self.get_name()


class Player(Entity):
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, hp, atk, defense):
        super().__init__(name, hp, atk)
        self.__defense = defense

    # TODO: Lengkapi getter
    def get_defense(self):
        return self.__defense

    # TODO: Lengkapi agar damage yang diterima dikurangi oleh DEF
    def take_damage(self, damage):
        defense = self.get_defense()
        current_hp = self.get_hp()
        if damage > defense:
            damage_defense = damage - defense
            new_hp = current_hp - damage_defense
        else:
            new_hp = self.get_hp()
        self.set_hp(new_hp)


class Boss(Entity):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    # TODO: Lengkapi agar damage yang diterima Depram tidak dipengaruhi
    #       oleh DEF
    def attack(self, other):
        current_hp = other.get_hp()
        damage = self.get_atk()
        new_hp = current_hp - damage
        other.set_hp(new_hp)


def main():
    # TODO: Meminta ATK dan DEF Depram
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))

    # Inisialisasi Depram dan musuh-musuh
    depram = Player("Depram", 100, atk, defense)
    enemies = [
        Entity(f"Enemy {i}", randint(20, 100), randint(10, 30))
        for i in range(randint(0, 1))
    ]
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10, 30)))

    print(f"Terdapat {len(enemies)} yang menghadang Depram!")
    print("------------")

    for enemy in enemies:
        print(f"{enemy} muncul!")
        print()
        print("---Status---")
        print(f"{enemy.get_name():20} HP: {enemy.get_hp()}")
        print(f"{depram.get_name():20} HP: {depram.get_hp()}")
        print("------------")
        while enemy.is_alive() and depram.is_alive():
            # TODO: Depram dan musuh melakukan attack dan print:
            #       Depram menyerang: "Depram menyerang {enemy} dengan {damage} ATK!"
            #       Musuh  menyerang: "{enemy} menyerang Depram dengan {damage} ATK!"
            depram.attack(enemy)
            print(f"{depram.get_name()} menyerang {enemy.get_name()} dengan {depram.get_atk()} ATK!")
            if not enemy.is_alive():
                break
            enemy.attack(depram)
            print(f"{enemy.get_name()} menyerang {depram.get_name()} dengan {enemy.get_atk()} ATK!")

        if not depram.is_alive():
            print("------------")
            print()
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f"{enemy} telah kalah!")

        print("------------")
        print()

    print("Selamat! Semua musuh Depram telah kalah!")


if __name__ == "__main__":
    main()