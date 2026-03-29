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

show beg at jump

a "I was curious if you'd be able to tutor me?"
"I desperately need to pass the next test!!"
"If I don't I won't be able to play in my next volleyball tournament!"





