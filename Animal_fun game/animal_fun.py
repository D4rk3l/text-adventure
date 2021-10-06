from sys import exit

def lion():
    print "You had to choose some direction and you chose West. You have been walking for miles.... and you're thirsty, and dehydrated."
    print "... you have just begun to feel you're walking into eternity when you see a T-junction. But just then you hear a ROAR!!!"
    print "You turn back to see a giant lion, miles away, running after you at great speed. You just have time to react. What now?"
    
    do_what = raw_input("> ")
    
    if "left" in do_what or "south" in do_what:
        print "Unfortunately for you, the lion catches up and rips you to shreds. You feel intense pain, yet you can't die. This is hell." 
        dead()
    elif "right" in do_what or "north" in do_what:
        print "You find a portal to another dimension. Could this be a trap? Or should you take that chance? What do you do?"
        do_what = raw_input("> ")
        if "portal" in do_what:
            cthulhu()
        else:
            dead()
    else:
        dead()

def princess():
    print "You have been walking for miles... and this is geting frustrating. Will this road ever end?"
    print "A dagger falls from the skies abvoe. What do you do?"
    do_what = raw_input("> ")
    if "dagger" in do_what or "pick" in do_what:
        print "lo and behold! A beautiful princess stands before you."
        print "A diamond on the hilt of your dagger turns the color of her eyes. This is a clue."
        what_color = raw_input("Do you see the color or blood?\n> ")
        print "... are you sexually attracted to her?"
        sexually_attracted = raw_input("> ")
        print "You'll have to make a choice. You can either go kiss in a warm embrace or kill her with your dagger. Which will it be?"
        your_choice = raw_input("> ")
        if "yes" in what_color or "blood" in what_color:
            if "kill" in your_choice:
                win()
            else:
                dead()
        elif "yes" in sexually_attracted:
            if "kiss" in your_choice:
                print "You have been betrayed by your lecherous lust. This goddess of desire turns into a dragon and burns you to dust."
                dead()
            else:
                win()
                
        elif "no" in sexually_attracted:
                if "kill" in your_choice:
                    print "What a muderous and sinful thing you did."
                    dead()
                else:
                    win()
        else:
            dead()
    else:
        print "You should have picked up the dagger. You never know what might be coming..."
        print "...but what do we have here!? A beautiful maiden! She looks like royalty. In fact she is a princess!"
        print "... are you sexually attracted to her?"   
        sexually_attracted = raw_input("> ")
        if "yes" in sexually_attracted:
            print "You have been betrayed by your lecherous lust. This goddess of desire turns into a dragon and burns you to dust."
            dead()
        else:
            print "The princess gives you a magic potion that can grant you any boon."
            print "You ask for all the happiness and riches of the world"
            win()                        

    
        
def prince():
    print "You have been walking for miles... and this is geting frustrating. Will this road ever end?"
    print "A dagger falls from the skies abvoe. What do you do?"
    do_what = raw_input("> ")
    if "dagger" in do_what or "pick" in do_what:
        print "lo and behold! A handsome prince stands before you."
        print "A diamond on the hilt of your dagger turns the color of his hair. This is a clue."
        what_color = raw_input("Do you see the color or blood?\n> ")
        print "... are you sexually attracted to him?"
        sexually_attracted = raw_input("> ")
        print "You'll have to make a choice. You can either go kiss in a warm embrace or kill him with your dagger. Which will it be?"
        your_choice = raw_input("> ")
        if "yes" in what_color or "blood" in what_color:
            if "kill" in your_choice:
                win()
            else:
                dead()
        elif "yes" in sexually_attracted:
            if "kiss" in your_choice:
                print "You have been betrayed by your lecherous lust. This god of desire turns into a dragon and burns you to dust."
                dead()
            else:
                win()
                
        elif "no" in sexually_attracted:
                if "kill" in your_choice:
                    print "What a muderous and sinful thing you did."
                    dead()
                else:
                    win()
        else:
            dead()
    else:
        print "You should have picked up the dagger. You never know what might be coming..."
        print "...but what do we have here!? A handsome prince!"
        print "... are you sexually attracted to him?"   
        sexually_attracted = raw_input("> ")
        if "yes" in sexually_attracted:
            print "You have been betrayed by your lecherous lust. This god of desire turns into a dragon and burns you to dust."
            dead()
        else:
            print "The prince gives you a magic potion that can grant you any boon."
            print "You ask for all the happiness and riches of the world"
            win()                        


def cthulhu():
    print "You walk for miles into what seems like an endless abyss. And then he presents himself. The evil Cthulhu."
    print "He, it, or whatever - stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        cthulhu()
        
def win():
    print "You made an excellent choice. You win. You are magically transported to your time, your world."
    print "Exit? (y / n)"
    exit = raw_input("> ")
    if "y" in exit or "Y" in exit:
        exit(0)
    else:
        start()        


def dead():
    print "Wrong move friend. You shall be lost forever into the infinite abyss of the tree of the undead."
    exit(0)

def start():
    print "You are walking through an enchanted forest with gigantic trees as tall as mountains and as thick as large lakes."
    print "You got here magically teleported into a distant planet in a distant galaxy in the future."
    print "You see one such tree with a cave-like structure at its base. What do you do?"
    
    do_what = raw_input("> ")
    
    while True:
        if "cave" in do_what or "cave-like" in do_what or "enter" in do_what:
            print "You enter  the dark hollow of an ancient tree that has had earthlings like you in the past."
            print "This tree is called the tree of the undying, where death won't touch you."
            print "On the other hand, pain can - if you don't make the right moves. And then you have to live with the pain for eternity."
            print "You are suddenly sucked into a vortex, finding yourself at crossroads of sorts." 
            print "From here, you can go north, south, east or west."
        
            while True: 
                now_what = raw_input("> ")
                if "north" in now_what:
                    cthulhu()
                elif "south" in now_what:
                    prince()
                elif "east" in now_what:
                    princess()
                elif "west" in now_what:
                    lion()
                else:
                    print "I got no idea what you're saying. Is it that hard picking a cardinal direction?" 
        else:
            print "I got no idea what you're saying. You have no choice but to enter the cave. Now let's start over"
            start()
            

start()    
