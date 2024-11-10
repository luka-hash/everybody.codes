with open("input2") as f:
        enemies = f.read()
        enemy_pairs = [(enemies[i*2],enemies[i*2+1]) for i in range(len(enemies)//2)]
        n_potions = 0
        potions_per_creature = {'A': 0, 'B': 1, 'C': 3, 'D': 5}
        for enemy_pair in enemy_pairs:
            match enemy_pair:
                case ('x', 'x'):
                    pass
                case (creature, 'x') | ('x', creature):
                    n_potions += potions_per_creature[creature]
                case (first_creature, second_creature):
                    n_potions += potions_per_creature[first_creature] + 1
                    n_potions += potions_per_creature[second_creature] + 1
        print(n_potions)

