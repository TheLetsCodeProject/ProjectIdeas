# Game Dev Ideas
***

## Rogue Like
These simple turns based games can be rather fun to play if done well. The focus of simple game play and depthful story to bring their world alive. Often these games hinge around survival and the hunt for resources. These games feature very simple retro art styles, but could also be done with more modern graphics. Examples include Dwarf Fortress and diablo

## Dungeon Adventure
Weather it be preprogrammed envrironments or procedurally generated dungeons, these games can be simple to implement. Using Unity's built in tile map functionalilty, construction of maps could be rather easy and quite enjoyable. The other consideration to keep in mind is the whilst the genre is 'dungeon', the games do not actually have to take place in a dungeon. An idea I've had is a top down mystery game set in an abandonned house. You must explore the house using your flash light to find clues for escape, all the while avoiding a monster.

## Left 4k Dead Clone
Recreate this simple game written by Notch in his pre-minecraft days. It has two mechanics: Walk and shoot.

## Bomber Man Clone
Not much to be said here. There are plenty of example of bomber man style games on the internet. Just google it.

## Don't move backwards
This game would be set in super simple mazes, the challenge is, you cant move backwards. This could become a super cool puzzle games as it could be possible to add special powerups which allow you to flip the orientation of the maze or even break certain walls. This could also be achieved using the unity tile engine. 

## Project Orbis 2: Prison escape
Continuing on the Orbis series, this game would be set in a prison world where your goal is to escape. This could involve complex level deign and various room based envrionments.

## Space invaders
Make a simple space invader clone or one that has an added twist. Maybe instead of your typical controls, you have to input a series of text based commands to move your character instead.

## CodeCraft
This game could directly incorperate a minecraft style UI, but instead of mining, you could use text commands to gain resources. Further through the game you could then create custom programs that completed tasks for you.. all with the goal of obtaining some moon rock or some other precious item.

## Sokoban style game
Look up sokoban.. chances are you've played a game like this before. It has simple mechanics but a lot of depth. All that is required is a player that can move certain parts of the environment to achieve a simple goal. This puzzle game could also be mixed with bomber man to create some interesting game play.

## Amibitious: Risk style game
This is not ambitious because of the gameplay, but due to the AI and board system needed to make this game play nicely. You'd most likely have to implement your own hex engine for this to work.

## Some form of base defence game
Whether it is a simple tower defence or more complicated base builder, this game could be fun to play. The game hinges around building up fortifications to defend a central position. This game would be even cooler if there was multiplayer capablilty allowing for two player to fight and attack eachothers bases whilst simultaneously defending their own

## Metroidvania
I don't actually know what makes a game classify as a metroidvainia only that these types of games can be cool. They typically cross features of a dunegon crawler with an endless runner style, all brought together wwith awesome retro style graphics

## Endless runner or Adventure runner
Games like "Thomas was alone" put an interesting spin of the old endless runner category, combining nuance with the old tropes.

## Craft/Build based RPG with quests

# NOTES:
All of these games could incorporate pieces of the OrbisEngines code base. Each one would require some level of research when it came to specific implementations of mechanics. It would also be very good to follow a more structured project architecture than we did for Orbis. Whilst Orbis was structured it did get a little messy towards the end. The development would have distinct stages and cycles. There would be three distinct categories of development: Engine (The technical and somewhat dirty stuff), Gameplay & State (Some harder parts, some easy. This is the code that the player directly interacts with) and Art & Audio (Which would most likely be a shared responsibilty). Using a 'manager' pattern is also a good ideas, as long as we ensure we have a 'ManagerManager' which is normally called a loader. The loader is responsible for reading configurations and then settting up all the manager instances accordingly.