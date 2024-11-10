with open("input1") as f:
        enemies = f.read()
        n_potions = 0
        for enemy in enemies:
            match enemy:
                case 'B':
                    n_potions += 1
                case 'C':
                    n_potions += 3
                case _:
                    pass
        print(n_potions)
