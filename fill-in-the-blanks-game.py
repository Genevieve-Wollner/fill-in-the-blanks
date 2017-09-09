from random import randint

# Easy-Stage song choices:
# Fresh Prince of Bel-Air Theme Song
# Friends Theme Song
# Spongebob Squarepants Theme Song
easy = ["""
In west ___1___ born and raised
On the ___2___ was where I spent most of my days
Chillin' out maxin' relaxin' all cool
And all shooting some ___3___ outside of the school
When a couple of guys who were up to no good
Started making trouble in my neighborhood
I got in one little ___4___ and my mom got scared
She said, "You're movin' with your ___5___ and uncle in Bel-Air."
""","""
So no one told you life was gonna be this way
Your job's a ___1___, you're broke
Your love life's D.O.A
It's like you're always stuck in ___2___ gear
When it hasn't been your day, your week, your ___3___
Or even your year, but

I'll be there for you
(When the ___4___ starts to pour)
I'll be there for you
(Like I've been there before)
I'll be there for you
('Cause you're there for me too)
""","""
Who lives in a ___1___ under the sea?
Spongebob Squarepants
___2___ and yellow and porous is he
Spongebob Squarepants
If ___3___ nonsense be something you wish
Spongebob Squarepants
Then drop on the deck and ___4___ like a fish
Spongebob Squarepants
"""]

# easy stage answers
correct_answers_easy = [["philadelphia","playground","b-ball","fight","auntie"],
["joke","second","month","rain"],
["pineapple","absorbent","nautical","flop"]]

# Medium stage song choices:
# Whip It, by Devo
# Ice Ice Baby by Vanilla Ice
# She Blinded Me With Science by Thomas Dolby
med = ["""
Crack that whip
Give the past the ___1___
Step on a crack
Break your ___2___'s back
When a ___3___ comes along
You must whip it
Before the ___4___ sits out too long
You must whip it
When something's going wrong
You must whip it
""","""
Yo, VIP, Let's kick it!!!!
Ice Ice Baby, Ice Ice Baby
All right stop, ___1___ and listen
Ice is back with my brand new ___2___
Something grabs a hold of me tightly
Then I flow like a ___3___ daily and nightly
Will it ever stop? Yo -- I don't know
Turn off the lights and I'll glow
To the extreme I rock a mic like a vandal
Light up a stage and wax a chump like a candle.
Dance, Bum rush the speaker that booms
I'm killing your brain like a ___4___ mushroom
Deadly, when I play a dope melody
Anything less than the best is a ___5___
Love it or leave it, You better gain way
You better hit bull's eye, The kid don't play
If there was a problem, Yo, I'll solve it
Check out the hook while my DJ revolves it
""","""
It's ___1___ in motion
She turned her ___2___ eyes to me
As deep as any ___3___
As sweet as any ___4___
Mmm, but she blinded me with science
She blinded me with science
And failed me in ___5___
"""]

correct_answers_med = [["slip","momma","problem","cream"],
["collaborate","invention","harpoon","poisonous","felony"],
["poetry","tender","ocean","harmony","biology"]]

# Hard stage song choices:
# Girl U Want by Devo
# Ninja Rap by Vanilla Ice
# Pulp Culture by Thomas Dolby
# I picked the same artists as medium difficulty for comedic effect.
hard = ["""
She sings from ___1___ you can't see
She sits in the top of the ___2___ tree
She sends out an ___3___ of undefined love
It drips on down in a ___4___ from above

She's just the girl, she's just the girl
The girl you want
She's just the girl, she's just the girl
The girl you want
""","""
YO! It's the ___1___ machine
Gonna rock the town without being seen
Have you ever seen a ___2___ Get Down?
Slammin and Jammin to the new swing sound
Yeah, everybody let's move
Vanilla is here with the New Jack Groove
Gonna rock, And roll this place
With the power of the ___3___ turtle bass
Iceman, ya know I'm not playin
Devastate the show while the ___4___ are sayin'
""","""
I drove all over Hollywood
Looking at the ___1___
First I ate my ___2___ Way
And then I ate my ___3___
But sucking on a Galaxy
I noticed something pretty bizarre
There's not a lot of ___4___ there,
Just an awful lot of ___5___, check it out
"""]

correct_answers_hard = [["somewhere","greenest","aroma","mist"],
["green","turtle","ninja","turtles"],
["stars","milky","mars","people","cars"]]

# String for the prompt at the start of the game to instruct and inform the user.
level_select_prompt = """
Welcome to my lyrical quiz!

Select your difficulty:
EASY: A familiar TV theme song.
MEDIUM: A popular one-hit-wonder.
HARD: A song by a one-hit-wonder band, that isn't their one hit wonder!
"""
# this is to establish what the 'blanks' function is looking for in the lines.
blank_prompts = ["___1___","___2___","___3___","___4___","___5___"]

# this function starts the game by generating a random value and giving the user
# one of three different games at the different difficulties.
def level_select():
    random_stage = randint(0,2)
    starting_input = raw_input(level_select_prompt)
    if starting_input.lower() == "easy":
        print easy[random_stage]
        return test_game(easy[random_stage],blank_prompts,correct_answers_easy[random_stage])
    if starting_input.lower() == "medium":
        print med[random_stage]
        return test_game(med[random_stage],blank_prompts,correct_answers_med[random_stage])
    if starting_input.lower() == "hard":
        print hard[random_stage]
        return test_game(hard[random_stage],blank_prompts,correct_answers_hard[random_stage])

# this checks if the current line contains a blank.
def blanks(line,blank_numbers):
    for prompt in blank_numbers:
        if prompt in line:
            return prompt
    return None

# this is the meat of the game, this function splits the song lyrics into lines
# then checks the content of those lines for blanks
# then prompts the user to fill those blanks. Rinse, repeat.
def test_game(game,blank_numbers,correct_answers):
    index = 0
    game = game.splitlines()
    for position, line in enumerate(game):
        current_question = blanks(line,blank_numbers)
        while current_question in blank_prompts:
            user_answer = raw_input("\nEnter answer " + current_question + ".\n")
            if user_answer.lower() in correct_answers[index]:
                line = line.replace(current_question,user_answer)
                current_question = line
                index = index + 1
            else:
                print "Try Again!"
        else:
            game[position] = line
            if current_question is not None:
                print "\n".join(game)

# I put this in to allow the user to play again if they want to!
if __name__ == '__main__':
    play_again = True
    while play_again == True:
        level_select()
        print "\n\nCongrats!"
        is_valid_input = None
        while is_valid_input != True:
            player_input = raw_input("\n\nWould you like to play again?\n\nYES/NO\n")
            if player_input.lower() in ["yes","y"]:
                is_valid_input = True
            elif player_input.lower() in ["no","n"]:
                play_again = False
                is_valid_input = True
                print "Thank you! Bye!"
            else:
                print "Sorry I don't understand! Try again?"
