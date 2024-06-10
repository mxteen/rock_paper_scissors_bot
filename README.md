# Telegram Rock-Paper-Scissors Bot

## Overview

This project is a Telegram bot that allows users to play "Rock, Paper, Scissors." It demonstrates working with standard buttons and project templates while providing a fun game.

## Features

- Sends a keyboard with buttons: Rock, Paper, Scissors.
- Generates a random choice from Rock, Paper, Scissors.
- Determines the winner based on the user's choice.

## Usage

### Starting the Bot

1. **Start the bot:** Send `/start` or find the bot in the search.
2. **Greeting:** The bot greets and offers to play, sending a keyboard with "Let's play!" and "Don't want to!" options.
3. **Help:** Send `/help` to read detailed rules.

### User Actions

1. **Press "Let's play!":**
    - Bot prompts: "Great! Make your choice!" and sends buttons "Rock", "Paper", "Scissors".
    - User selects an option, bot generates its choice, announces the winner, and offers to play again.
2. **Press "Don't want to!":**
    - Bot replies: "Okay. If you want to play, press 'Let's play!'".
3. **Send `/help`:**
    - Bot sends game rules and offers to play.
4. **Send any other message:**
    - Bot replies it doesn't understand the message.

## Commands

- `/start` - Start the bot and get a greeting with an offer to play.
- `/help` - Get the game rules and an offer to play.

## Game Rules

- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.

Enjoy playing "Rock, Paper, Scissors" with the bot!