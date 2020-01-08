#--- Developers: Group 2 (Errol, Mark, Mohammed, Uganbatbatsukh)
#--- Date: TBA
#--- Game Name: Love's Murder

# Global imports
import time
import random

sleep_timer = 1

#--- Useful Functions for later
def cls():
    print('\n' * 25)

# Scene 1
yes_no = ["enter", "leave"]

def introduction():

    name = input("What is your name, unfortunate guest?\n \n")
    print("\nRespects , " + name + ". You were crazy enough to agree to come to this party.\n \nNow let's find out if they've left anything for you in the will!\n")
    time.sleep(2)
    print("You get out of your small fiat panda and, cant help but admire the once majestic\nmansion you use to visit so often in your childhood.")
    time.sleep(2)
 
# Responce to entering mansion
    response = ""
    while response not in yes_no:
        response = input("\n \nDo you go back, or follow through\n \nenter/leave : ")
        if response == "enter":
            print("\n \nYou head into the party. You hear ominous crows cawwing in the distance.\n")
        elif response == "leave":
            print("\n \nYou are not ready for this particular journey in your life. Goodbye, " + name + ".")
            quit()
        else: 
            print("I didn't understand that.\n")
         
introduction()
#time.sleep(3)


# Scene 2

drinks = ["water", "punch", "gin"]
def scene_one():
    cls() 
    print('''You are escorted in to a entertaining room and spot 4 familiar figures;''')
    time.sleep(sleep_timer)
    print('''\n> A Red Haired Women. Attractive with sturdy pose, you dont recognise her''')
    time.sleep(sleep_timer)
    print('''\n> Cousin Alan being socially awkward as usual, humming to himself in the corner''')
    time.sleep(sleep_timer)
    print('''\n> Boistrous Maxie, playing pool''')
    time.sleep(sleep_timer)
    print('''\n> And the countess of the mansion Lizzie; decked with her extravigant jewels ''')
    time.sleep(sleep_timer)
    print('''\n \nYou decide to get a drink to take the edge off your nerves
        before aproaching your cousins.
         
        > Have a glass of water
        > Try some punch
        > Gin & Tonic''')
  
    responce = ""
    while responce not in drinks:
        responce = input("\n \nWhat drink do you take (water/punch/gin): ")
        cls()  
        if responce == "water":
            print("\n \nYou stomach churns, you begin to feel drowsey.\n \n")
        elif responce == "punch":
            print("\n \nYou feel a sharp pain before collapsing, someone calls out your name!.\n \n")
        elif responce == "gin":
            print("\n \nYou taste something sour and it isnt the lemon!, there are\n others collapsing around you....\n \n")    
        else: 
            print("\n \nI didn't understand that.")
                  
scene_one()
#time.sleep(3) 


#Scene 3

def scene_three_choices():

    paths = ["a", "b","c"]

    
    print('''You wake up blurry eyed shocked from the screams taking place
    around you. You check you pockets and find your mobile has been taken. The
    telephone line also is cut off...
    \nThere is also a large thumping noise coming from somewhere upstairs. Something
    is clearly very wrong here...\n''')
    time.sleep(sleep_timer)
    print('''As you stagger to your feet alarmed at the sound of the screams, you notice
    that there is also a trail of blood leading into the corridor...''')
    time.sleep(sleep_timer)
    print('''What is your choice of action?\n

    a) Follow the sounds of the Screams

    b) Examine the trail of blood

    c) Ivestigate the source of the thumping sounds coming from upstairs''')

    responce = ""
    while responce not in paths:
        responce = input('\n \n \nEnter option choice (a,b,c) : ')
        cls()  
        if responce == "a":
            
            screams_celler()
        elif responce == "b":
            
            blood_kitchen()
        elif responce == "c":
            
            thumping_attic()
        else: 
            print("\n \nI didn't understand that.")
                  

                
# cellar

def screams_celler():
    start_room_options = ['1','2','3']
    user_choice=''

    while user_choice not in start_room_options:
        
        print('''You follow the sounds of the screams to the door of a wine cellar.\n
\nYou take a moment and then open the door...''')
        time.sleep(2)
        print('''\n \nA horde of hellium inflated birthday balloons fly out. Curriously, the
birthday balloons have 'Edward' printed on them.\nHmm Edward is the name of your cousin who died from a riding
accident 6 years ago...''')

        time.sleep(2)
        print('''\nOnce you clear the ballons, you discover the source of the screams....''')

        time.sleep(2)
        print('''\nLying on the floor is a Alexa Soeaker, playing a playlist of
classic horror film screams.
\nFirst the spiked drink, than the balloon and now this sick recording...

Is this all a messed up prank/trick?

You break the Alexa speeker by kicking it agisnt the wall in frustration.

\n \nWhat is your next course of action

1)Examine the trail of blood leading down the corridor

2)Go find the source of the continous thumping noise

3)Escape''')
        
        user_choice = input('\n \nEnter option number: ')

    #print('You have selected ' + user_choice)

        if user_choice == start_room_options[0]:
            blood_kitchen()
        elif user_choice == start_room_options[1]:
            thumping_attic()
        elif user_choice == start_room_options[2]:
            print('Game Over! You saved your bacon but what about your cusins?')
        

#Kitchen 
def blood_kitchen():
    drinks = ['continue', 'leave']
    cls()
    print('''You've followed the trail of the blood from the corridor to the open kitchen.''')
    time.sleep(2)
    print('''\n\nThe blood leads to a meat locker. You take a deep breath and slide open the door.'''
    '''\n \nYou are horrified at the seight of a bloody body laying across the floor.''')
    time.sleep(3)
    print('''\nYou rush to check the pulse''')
    time.sleep(3)
    print('''\nIt's too late, your aunt Lizzie is dead and frozen to the touch.''')
    time.sleep(2)
    print('''\nYou feel a mix of emotions rush to you head; fear, grief and anger as you notice
that the culprit used the crowbar for hideous crime.\nYou wrap a towel around the crowbar and pick
it up for protection. 



There is also blood on the wall read what seems to be SORRY S''')
    time.sleep(4)
    print('''\n \nWhat do you do now ?

> Find the source of the thumping noise

> Leave the mansion

> Go to source of Screams''')

    responce = input("\n \nWhat do you investigate now ? (attic/leave/cellar): ")
    cls()  
    if responce == "attic":
        thumping_attic()
    elif responce == "leave":
         print("\n \nYou Leave, Game Over! You live out the rest of you life with deep rerets.\n \n")
    elif responce == "cellar":
         screams_celler()
    else: 
         print("\n \nI didn't understand that.")

# Attic
def thumping_attic():
    print("                        ######BANG!!######                    ")
    time.sleep(1)
    print("                        ######BANG!!######                    ")  
    time.sleep(1),
    print("                        ######BANG!!######                    ")

    print('''\nYou arrive at the attic to find the others alive but arguing. You also
notice Maxie is having a seizure and is the cause of the thumping noise. You
rush over and put Maxie in the recovery position.


After making sure Maxie is safe. You get to the source of the arguement.
It turns  out Edward's death was staged for insurance purposes.

He seems to have orchestrated these horrific events and murdered his mother in
a act of maddness. 

After questioning your cousins you find out that he is currently in the shed with a
hostage who is tied up. All of you agree to save the hostage and head over to
the shed to stop the Edward. 

''')

scene_three_choices()

def shed():    
    cls()
    print('''As the door is locked from the inside we manageded kick the door down,
and are horrified to find Edward standing over the tied hostage with a machete.

One of the ladies start talking to Edward, he takes notice and starts to calm down.

In shame, he drops the machette and holds his head in his hands.

He then reaches for his pocket, we all take cover!

Luckily it is a mobile phone. He then calls the police....''')

time.sleep(20)
shed()



    

    



    


