# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sammy")
define a = Character("Angie")
define n = Character(" ")
define b = Character("Girls")
define c = Character("Teacher")



    
# The game starts here.

label start:

scene nurse

s "Sammy wait!"

scene classroom
with fade

show sadsammy at right
c "Bla bla bla"

n "..."


show chill  at left
with easeinleft
a "Psttt Pstt"

s "Huh..?"

a "Hey! You're like super smart right?"
show annoyed
s "Oh. I guess."

a "Right.. Well! a my name is Angie, It's nice to meet you"

s "Nice to meet you too, what do you--"

show beg 
with easeinbottom

a "I was curious if you'd be able to tutor me?"
a"I desperately need to pass the next test!!"
a"If I don't I won't be able to play in my next volleyball tournament!"

s "Ah. And why is that my problem?"
show nervous
a "Because uhm.. Uhm.. I-- I'll pay you! 50 dollars per session!"

menu:

    "Should Sammy help her?"

    "Yes":
        s "Fine.. I guess I could help"
        jump yes
    "No":
        s "No. Leave me alone"
        jump No

label No:
scene classroom
show beg
a "Awh man.. That's alright thanks though."

return



label yes:

scene classroom
show kiss
show annoyed 
a "YAY! You're saving my--"
c "Quiet back there!"
show nervous
a "Ah-- my bad heh"
show chill
a "Can you meet tomorrow at the library???"

show sammyblush
s "Yeah I can. See you then "

scene library
with fade 

show sadsammy at left

s "I wonder when she'll get here she said--"

show boo 
with moveinleft

a "BOO!"

show scared

s "AH!"
hide boo
"shhh!"

show angry 

a "What the heck man!"

show nervous 

a "Heh, sorry.. hehe"

s "That's it! I'm not helping you we should whisper instead."

return







