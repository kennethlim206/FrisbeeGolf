Last motified: 11/23/13

Frisbee Golf Championships Game

Welcome to the Frisbee Golf Championship Game. You are a talented Frisbee
Golfer facing the reigning world Frisbee Golf Champion (Beau Kittridge). Beau is the
reigning world champion because of his powerful and accurate throws at close and long range.
He will not miss when he has no obstacles in his way. However, when it comes to obstacles
he has trouble throwing around them and will sometimes put too much power on the frisbee and
throw it out of bounds. While you might not possess Beau's strength, you can use your
Frisbee Golf skills to navigate these difficult obstacles and become the new champion
of the world! Good luck and have fun.

Main menu:
The main menu screen will create 3 different courses for you to play on based on difficulty.
Winning one level does not mean that you move on to the next level, you have to click the
"reset" button if you have won one level and want to play another. Scores also do not carry
over from one game to another.

Controls:
The 3 buttons in the top-left corner of the screen control power. Clicking one will change
the amount of power that is put on the frisbee, but clicking a power button will not
throw the frisbee.

The direction buttons in the bottom-left corner of the screen control the direction that
the frisbee is thrown, and clicking one of these will throw the frisbee.

You can also go back to the main menu by clicking the "reset" button, or quit the game by
clicking the "quit" button.

The display in the top-right corner of the screen keep track of the par for a particular
course and the number of moves that you have used. As a mercy rule, the game will quit
automatically after 25 moves.

Obstacles:
Grey rectangles on the screen are mountains and if your frisbee lands on one of these, you
will automatically lose the game.

Blue rectangles are lakes and if your frisbee lands in a lake, you will also automatically
lose the game.

The light-brown/orange rectangles are sand bunkers. If your frisbee lands in a bunker, your
throwing power will significantly decrease until you can escape the bunker.

Computer Player (black frisbee):
In tribute to the current best Ultimate Frisbee player in the world, I have named my
computer player Beau. Beau is not very good at finding the gaps between
obstacles. Instead, he just throws south until he will not hit any obstacles when he throws
forward. He can throw a lot farther than you, so even though he doesn't move forward for
the first few turns, he can still catch up very quickly. He has so much power on his throws
that bunkers will affect you more than him. However, because he has so much power his throws
are somewhat inconsistant. Every time he throws there is a 25% chance that his throw will
be too strong and have double the power that he intended. This means that Beau will
sometimes throw his frisbee out of bounds. Beau also becomes very accurate when he has
gotten past all obstacles, and will score in two throws if he has a direct line to the goal.

Scoring:
As soon as your frisbee touches the goal (yellow circle), then the round will end and you
will be notified whether you have gotten under par or not. If you and Beau both throw into
the goal at the same time, you will win the round.

If Beau throws his frisbee out of bounds, you can continue to play, but if you throw out
of bounds then the round ends.

Construction:
My program starts with classes for power buttons, direction buttons, obstacles, the
displays that appear at the end of the game and the goal. These classes do not give function
to these buttons or objects, they just take a center point, length and width
for the button's creation and then have draw, undraw and clicked methods.
The difference between power and direction buttons is that power buttons take a "power"
value from the Game class that will multiply the movement of the frisbee by that value later.

The obstacles are the same except instead of a clicked method, they have a method that will
return a list of their x and y mins and maxes so I can determine whether the frisbee
has landed on a certain obstacle.

I have a rules class. This class keeps track of the current position of both frisbees. It
also has variables that will change based on if the frisbee has gone out of bounds, scored,
etc. If one of these variables changes, it activates a display in the Game class that tells
the user if he has gone out of bounds, won, etc. The rules class also keeps track of the
number of moves that both players have taken. 

The game class is where I give functions to all of my buttons and obstacles. It starts by
making the window and then makes the main menu buttons. Once a difficulty is selected, it
creates the correct course for that difficulty and then makes the buttons and frisbees.
Then there is a play method that goes through each turn and moves the frisbee based on the
buttons the user pushes, checks if the user has won or lost, and then moves the computer
player. The play method also is responsible for creating the displays once the user or
computer has won or lost.

The game class's last element is the computer player method. It tells the computer player
where to move each turn and also checks whether the computer player has won or lost each
turn.

Status:
My program currently is finished. I have played it many times. The controls are easy to
use and I haven't found any glitches. The computer player could be more intelligent, but I
found it too complicated to make a more intelligent computer player. I originally didn't want
a player that would do the same thing every time, so I was going to have the computer move
randomly based on a random number generator, and then try and avoid obstacles as it got
within a certain distance of that obstacle, but because it moved randomly, there were too
many scenarios when the computer player would crash because it would be too close or too
far from the obstacle to "see" it. Also, this method made the computer player move very
slowly, and while I think I would have eventually been able to get it to move randomly
and also avoid obstacles, it would not have done it in a reasonable number of moves.

I decided to make the computer player just avoid obstacles entirely, by starting off each
round by going lower than the lowest obstacle and then going forward. This made the computer
player go very quickly, but also made it do the same thing every time. To add some variation
I added the random number generator component, but made it affect the power, no the direction
of the computer player. The result is a computer player that has the ability to beat you
to the goal, but also can crash or take a long time to reach the goal. These three
scenarios happen about the same amount, which gives me the variation I wanted so I am
happy with the way it turned out.

Besides the intelligence of the computer player, I was able to perform all the functions I
wanted to perform to make the game. I am happy with the finished product.
