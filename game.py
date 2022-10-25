import random

# GAME:
# Play as an alien that is trying to
# catch his friends as they fall from above

# Fun tasks to try out yourself:
# 1) Change images (background, alien, alien friend) to create a completely new game
# 2) Change the win screen font by adding special effects that you can find in the docs (see slides)
# 3) Add health to the player. If the player loses all health, show the lose screen.
# 4) Add a falling enemy. If the player catches the enemy, they lose health OR lose score.

###########
# VARIABLES
###########

# Regulates the screen dimensions
WIDTH = 700
HEIGHT = 500

# Background color
bg_color = (149, 200, 222)

# All the sprites that we will use
alien = Actor("alien", pos=(WIDTH / 2, HEIGHT - 60))
alien_friend = Actor("alien_hurt")
background = Actor("space_background")

# Miscellaneous variables, the name speaks for itself
alien_speed = 5
friend_speed = 5

friend_random_dir = 0

score = 0

num_to_win = 10

we_won = False

###########
# FUNCTIONS
###########

# Called by Pygame Zero when it needs to redraw your window
def draw():
    global score, we_won

    screen.fill(bg_color)

    # Order of sprites matters.
    # If you draw the alien and then the background,
    # the background will completely hide your alien behind it
    background.draw()
    alien.draw()
    alien_friend.draw()

    # Draw caught friends counter
    score_text = "Score: " + str(score)
    screen.draw.text(score_text, (0, 0), fontsize=40)

    # Win condition
    if we_won:
        screen.fill(bg_color)
        screen.draw.text("You won!", center=(WIDTH/2, HEIGHT/2), fontsize=150, shadow=(0.5, 0.5), color="orange", gcolor="white")

# Update function is called repeatedly, 60 times a second
# Called by Pygame Zero to step through your game logic
def update():
    # Global variables that we will modify in this function
    global score, we_won

    # PLAYER MOVEMENT
    if keyboard.right:
        # Notice that alien.x += alien_speed
        # is the same as alien.x = alien.x + alien_speed
        alien.x += alien_speed

        # If player goes off the right side of the screen
        # Make them appear on the left side
        if alien.left >= WIDTH:
            alien.right = 0

    if keyboard.left:
        alien.left -= alien_speed

        # If player goes off the left side of the screen
        # Make them appear on the right side
        if alien.right <= 0:
            alien.left = WIDTH

    # FRIEND FALLING MOVEMENT
    # The friend will constantly fall down with the speed of "friend_speed"
    # The friend will randomly fall slightly left or slightly right
    # "friend_random_dir" regulates the slight random horizontal fall
    # see reset_alien_friend() function for details on how it's implemented
    alien_friend.y += friend_speed
    alien_friend.x += friend_random_dir

    # If alien friend went out of bounds
    if alien_friend.y > HEIGHT:
        score -= 1
        reset_alien_friend()

    # If we caught the alien friend!
    if alien.colliderect(alien_friend):
        score += 1
        reset_alien_friend()

    # Keep track of whether we caught enough friends to win
    if score >= num_to_win:
        we_won = True

# Our own function. It's only called when we specifically call it in our code
# Resets the position of the alien friend and
# puts them at a random position off the top of the screen
def reset_alien_friend():
    # Global variables that we will modify in this function
    global friend_random_dir

    new_x_pos = random.randint(0, WIDTH)
    new_y_pos = -50

    alien_friend.x = new_x_pos
    alien_friend.y = new_y_pos

    # To make our alien friends fall in different directions
    # decide on a random floating point number between a specified range
    friend_random_dir = random.uniform(-1.5, 1.5)
