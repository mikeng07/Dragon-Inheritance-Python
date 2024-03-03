import hero
import dragon
import fire_dragon
import flying_dragon
import random
import check_input

def main():
    name = input("what is your name, challenger? \n")
    hero1 = hero.Hero(name, 50)
    dragons = [dragon.Dragon("Deadly Nadder", 10), fire_dragon.FireDragon("Gronkle", 15), flying_dragon.FlyingDragon("Timberjack", 20)]
    print ("Welcome to dragon training, " + hero1.name +"\n"+
            " You must defeat 3 dragons \n" )

    while hero1.hp > 0 and len(dragons) >0:
        print(hero1)
        for i,d in enumerate (dragons):
            print(str(i+1) + ". " + str(d))

        drag_choice = check_input.get_int_range(" Choose a dragon to attack: ", 1, len(dragons))

        print("\nAttach with \n"+
                "1. Arrow (1 D12)\n"+
                "2. Sword (2 D6)")
        
        weapon_choice = check_input.get_int_range("Enter weapon: ", 1,2)

        #hero attacks dragon
        print (hero1.arrow_attack(dragons[drag_choice - 1])) if weapon_choice == 1 else print (hero1.sword_attack(dragons[drag_choice - 1]))
        # attack the dragon of choice from dragons list
        # print the arrow_attack function

        dragons.pop(drag_choice - 1) if dragons[drag_choice - 1].hp == 0 else None
        # remove dragon from list if it's dead

        # get random dragon attack if there is any
        if len(dragons) > 0:
            rand_dragon = random.randint(0, len(dragons) - 1)
            rand_attk = random.randint(1,2)

            if rand_attk == 1:
                print(dragons[rand_dragon].basic_attack(hero1))
            else:
                print(dragons[rand_dragon].special_attack(hero1))

    # GAME OVER
    if hero1.hp == 0:
        print("The dragons have slain you!\n"+
                "Game over.")
    else:
        print("Congratulations! You have defeated all three dragons, you have passes the trials. ")

main()