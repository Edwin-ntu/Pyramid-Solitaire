# Pyramid-Solitaire
This is code I made in the first year of university, command line game of pyramid solitaire.
Below this text is a description of what pyramid solitaire is - this is what I used to base my game logic on.

What is Pyramid Solitaire?

Pyramid solitaire is a game of cards that you play on your own with a standard pack of 52 cards. It’s easy to learn the rules, and to become a successful player, all you need is basic logic skills.

The Goal

The goal of this version of solitaire is to remove all the cards from the pyramid pile of cards. Points are awarded to players who successfully compare and remove cards from any accessible pile of cards – more points are awarded to players who remove harder to access cards.

The Set Up

To set the game up, you shuffle a pack of cards split it into two piles. One pile of 28 cards is called the pyramid pile, and the rest of the cards are placed in the stock pile. The pyramid pile is the arranged in a way that one card is placed on its own, then two more are placed underneath it, with each row underneath having one more card in it until a pyramid is formed – like this one below:

Removing Cards

To complete the game, all the cards in the pyramid must not remain. To remove cards from the pyramid, you must compare two cards with each other. If their sum is 13, they can be removed together. However, only certain valid cards can be used for comparisons.

Valid Cards

Any card that doesn’t have another card beneath it partially are valid. Therefore, at the start of the game, the seventh row can be accessed along with the top of the stock pile, but no other card can be. To access other cards from the pyramid, the two cards beneath it must be eliminated. Other cards in the stock pile can be accessed by milling the top stock card and moving it to the waste pile. This reveals the second card on the pile for access. The top most card on the waste can also be accessed.

The Stock and Waste

At the start of the game, the stock is a pile of 24 cards that is placed face up near the pyramid. The top card can be used in comparisons, or be placed on the top of the waste pile. If one doesn’t exist yet, the card becomes the waste pile. When all the stock is either milled or compared, the waste is then turned into the stock again by reversing the pile and placing it where the stock was. This can happen indefinitely.
