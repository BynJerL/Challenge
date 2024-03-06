import random as rd
from time import sleep

playerMaxHp = 20
playerHp = playerMaxHp
playerPow = 3
enemyMaxHp = 15
enemyHp = enemyMaxHp
enemyPow = 4

isPlayerTurn = True

while True:
    if enemyHp <= 0:
        enemyHp = 0
        print("Enemy Down!")
        sleep(1)
        print("Player Wins")
        break
    if playerHp <= 0:
        playerHp = 0
        print("Player Down!")
        sleep(1)
        print("Enemy Wins")
        break

    if isPlayerTurn == True:
        print("\nPlayer\' Turn")
        print(f"Player (HP: {playerHp}/{playerMaxHp}, POW: {playerPow})\nEnemy (HP: {enemyHp}/{enemyMaxHp}, POW: {enemyPow})")
        sleep(1)

        while True:
            action = str(input("Action (\'a\' for attack, \'h\' for heal, \'n\' for none):\n"))
            
            if action in ['a', 'attack']:
                dmg = rd.randrange(-1, playerPow) + 1
                enemyHp -= dmg
                print(f"You\'ve drained {dmg} HP from the enemy...")
                break

            elif action in ['h', 'heal']:
                heal = playerPow - 1
                
                if (playerHp + heal) > playerMaxHp:
                    heal = playerMaxHp - playerHp
                    playerHp = playerMaxHp
                else:
                    playerHp += heal

                print(f"You\'ve restored {heal} HP...")
                break

            elif action in ['n', 'nothing', 'none']:
                print(f"You\'ve decided to do nothing...")
                break
    else:
        print("\nEnemy Turn")
        sleep(1)

        enemyPossibleActions = ['a','a','a','a','a','h','h','n'] if (enemyHp < enemyMaxHp) else ['a','a','a','a','a','a','n','n']
        enemyAction = rd.choice(enemyPossibleActions)

        if enemyAction in ['a']:
            dmg = rd.randrange(-1, enemyPow) + 1
            playerHp -= dmg
            print(f"Enemy has attacked player! Player has lost {dmg} HP...")

        elif enemyAction in ['h']:
            heal = enemyPow - 1
            
            if (enemyHp + heal) > enemyMaxHp:
                heal = enemyMaxHp - enemyHp
                enemyHp = enemyMaxHp
            else:
                enemyHp += heal
            
            print(f"Enemy has released heal spell!, restore {heal} HP to enemy...")

        elif enemyAction in ['n']:
            print("Enemy didn\'t take any action...")
            pass
    
    sleep(1)
    isPlayerTurn = not isPlayerTurn