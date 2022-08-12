"""
Okay so you need to create a simple program which is called number guesser
We will build a nice application in a few iterations
Here is a logic:
1. Define a variable with a random number in range from 1 to 10 (you will need in-built random module)
2. Take a user guess as an int (you will need an input function)
3. Compare 2 numbers, if they are the same, print some hooray text, else some sad text
"""

# A place for a code


"""
    As you can see, you can make only 1 guess in 1 program run, that's not so cool
    Now change your program so you can make infinite amount of attempts, so you can finally guess it
    P.S. You will need a while loop
"""

# A place for a code


"""
    Now limit amount of attempts to a certain number, let's say 3
"""

## A place for a code


"""
    Okay, I hope it's working, now try to input not a number, for example letter E
    Yeah, you will to handle this "exceptional" situation ;)
    For this you will need a function, let's call it get_user_input
    Function should not have any arguments, and return a guess as an int, you should ask for an input until input is valid,
    so yeah while loop once again :)
    Now use this function inside your loop to receive an input
"""

# A place for a code


"""
    Now let's upgrade our main while loop, by replacing it with for loop
    You will need range function to make limited amount of iterations (one iteration for each attempt)
"""

# A place for a code


"""
    Okay so now we have some decent work done and game is working
    As an extra task you can think about how you can create a class which will receive a max possible number
    And amount of allowed attempts, class should have a .run method which will launch gaming process
    so you will have smth like
    game = GuessGame(max_number=11, attempts_allowed=3)
    game.run()
"""

# A place for a code
