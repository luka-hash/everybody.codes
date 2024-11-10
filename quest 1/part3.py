with open("input3") as f:
        enemies = f.read()
        enemy_pairs = [(enemies[i*3],enemies[i*3+1],enemies[i*3+2]) for i in range(len(enemies)//3)]
        n_potions = 0
        potions_per_creature = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
        for enemy_pair in enemy_pairs:
            match enemy_pair:
                case ('x', 'x', 'x'):
                    pass
                case (creature, 'x', 'x') | ('x', creature, 'x') | ('x', 'x',creature):
                    n_potions += potions_per_creature[creature]
                case ('x', first_creature, second_creature) | (first_creature, 'x', second_creature) | (first_creature, second_creature, 'x'):
                    n_potions += potions_per_creature[first_creature] + 1
                    n_potions += potions_per_creature[second_creature] + 1
                case (first_creature, second_creature, third_creature):
                    n_potions += potions_per_creature[first_creature] + 2
                    n_potions += potions_per_creature[second_creature] + 2
                    n_potions += potions_per_creature[third_creature] + 2
        print(n_potions)

