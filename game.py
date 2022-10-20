import random

# GAME:
# Play as an alien that is trying to
# catch his friends as they fall from above

# Tasks for the participants:
# 1) Change images (background, alien, alien friend) to create a completely new game
# 2) Change the win screen font to be like what I have in the demo (color gradient, drop shadow, included in this code)
# this is to get them to read docs
# 3) Add health to the player. If the player loses all health, show the lose screen.
# 4) Add a falling enemy. If the player catches the enemy, they lose health OR lose score.

###########
# VARIABLES
###########

# Regulates the screen dimensions
WIDTH = 700
HEIGHT = 500

# Background color (for the first part of the lesson)
bg_color = (149, 200, 222)

# All the sprites that we will use
alien = Actor("alien", pos=(WIDTH / 2, HEIGHT - 60))
alien_friend = Actor("alien_hurt")
background = Actor("space_background")

alien_speed = 5
friend_speed = 5

friend_random_dir = 0

num_of_caught_friends = 0

num_to_win = 10

we_won = False

###########
# FUNCTIONS
###########

# Called by Pygame Zero when it needs to redraw your window
def draw():
    global num_of_caught_friends, we_won

    screen.fill(bg_color)

    # Order of sprites matters
    background.draw()
    alien.draw()
    alien_friend.draw()

    # Draw caught friends counter
    score_text = "Score: " + str(num_of_caught_friends)
    screen.draw.text(score_text, (0, 0), fontsize=40)

    # Win condition
    if we_won:
        screen.fill(bg_color)
        screen.draw.text("You won!", center=(WIDTH/2, HEIGHT/2), fontsize=150, shadow=(0.5, 0.5), color="orange", gcolor="white")

# This is called repeatedly, 60 times a second
# Called by Pygame Zero to step through your game logic
def update():
    # Global variables that we will modify in this function
    global num_of_caught_friends, we_won

    # PLAYER MOVEMENT
    if keyboard.right:
        alien.x += alien_speed

        # If player goes off the right side of the screen
        # Make them appear on the left side
        if alien.left >= WIDTH:
            alien.right = 0
    elif keyboard.left:
        alien.left -= alien_speed

        # If player goes off the left side of the screen
        # Make them appear on the right side
        if alien.right <= 0:
            alien.left = WIDTH

    # FRIEND FALLING MOVEMENT
    # Random direction may or may not be added (x movement)
    # depends on the prior coding experience of the group
    alien_friend.y += friend_speed
    alien_friend.x += friend_random_dir

    # If alien friend went out of bounds
    if alien_friend.y > HEIGHT:
        num_of_caught_friends -= 1
        reset_alien_friend()

    # If we caught the alien friend!
    if alien.colliderect(alien_friend):
        num_of_caught_friends += 1
        reset_alien_friend()

    # Keep track of whether we caught enough friends to win
    if num_of_caught_friends >= num_to_win:
        we_won = True

# Our own function
# Reset the position of the alien friend
# Put them at a random position off the top of the screen
def reset_alien_friend():
    # Global variables that we will modify in this function
    global friend_random_dir

    new_x_pos = random.randint(0, WIDTH)
    new_y_pos = -50

    alien_friend.x = new_x_pos
    alien_friend.y = new_y_pos

    # To make our alien friends fall in different directions

    friend_random_dir = random.uniform(-1.5, 1.5)
