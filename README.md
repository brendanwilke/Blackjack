# Blackjack

**Description**

This program is a text-based representation of the classic Blackjack card game. The player and the dealer both start with 2 cards each. The player can check is able to check their cards whenever, and sees all but one of the dealer's cards at a time. The player will be prompted to hit or stand until they decide to stand. The person closest to reaching a total value of 21 between all their cards is the winner.

**Necessary Installations**
* Python 3

**Usage**

The values given to each card type are:
* One: 1
* Two: 2
* Three: 3
* Four: 4
* Five: 5
* Six: 6
* Seven: 7
* Eight: 8
* Nine: 9
* Ten: 10
* Jack: 10
* Queen: 10
* King: 10
* Ace: 1 or 11 (11 is the default but automatically switches to 1 if the player would bust with 11)

The player start with 100 chips and will be prompted to enter an amount of chips they would like to bet on. After that, the first 2 cards will be dealt to the player and the dealer. The player will be see their cards and all but one of the dealer's cards every round. After seeing the cards, the player will be prompted to hit (take another card) or stand (stop receiving new cards). If either the player or the dealer hit and go over 21 with their combined value of cards, they bust and the other one wins. Otherwise, the player closest to a combined card value of 21 wins the chips. There are also potential cases for a tie where no chips are won or lost.
