
# Snake & Ladder

A classic Snake and Ladder game on CLI.

## Features

- Command line base light weight game.
- Easy user interface
- Multiple player can play.
- Cross platform





## Documentation

This project is aimed at developing a multiplayer Snake and Ladder game,
whick can be played on commad line. This game has been built using Python.

Libraries Used:
    1. random : This library helps to choose an element randomly among a
    given list or to get a random number or shuffle elements randomly.
    I used this library to choose a random
    number from 1 to 6, as in a dice.

    2. time : This library provides various time-related functions.
    I used the sleep method of this library to make the user experience
    of this game better.

Modules:

    1. player: I create this module for creating players and storing their name
    and score.
    This module has a class Player, with two attributes
    self.name and self.point, and a method, create_players()

    2. snake: This modeul is to create snakes and check if a certain position
    has head of a snake.
    It has a class Snake with two method check_snake() and create_snake()
    and an attribute self.snakePosition.

    3. ladder: This module deals with the ladders of the game.
    It has a class Ladder. And this class has two method check_ladder()
    and create_ladder(), and an attribute self.ladderPosition.


functions:

    1. play: This is the main function of the game. All the game
    functionality is written here.
    This function has been called under a while loop.

    2. dice: This function roll the dice and return the result.
