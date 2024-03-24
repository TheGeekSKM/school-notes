@Programmer 
# Tasks

*Note: The tasks for this week will be different. I will not assign them individually but I will assign them to the different teams (GM1, GM2, Core, etc). The programmers in those teams can decide which task you would like to take on (please let the other programmers in your team know). On Trello, these task cards will be assigned to all the programmers in the team, and when you are working on it, just move it around as you see fit.*

### All these tasks MUST be completed by 02/12 (Monday) at 11:59pm. I will be making a build early Tuesday Morning :)

## __**GameMode 1:**__ @skinnygoblin, @bobystar    
1. Particle System follows the player in 1st place *(in terms of points)*
2. Spotlight now follows player with the crown
3. Implement or Check VO Events when I give you the list

## __**GameMode 2:**__ @stardream09, @surilexa  
1. When a player falls off the map, they should not lose any stars
2. Finish connecting DA_Trail to the Trail Niagra System *(Since you were already working on this, Jacob, I'd recommend just continuing on it :) )*
3. On Player vs Player Collision: the player that is dashing should steal stars from the player that isn't (I'd recommend making the # of stars stolen a variable in a Data Asset). If both players are dashing, they just trade stars.
3. Implement or Check VO Events when I give you the list

## __**Core:**__ @thegeekskm, @veryhuman  
1. Sai: PLEASE FIX THE RESULTS SCREEN DEAR GOD IN HEAVEN PLEASE
2. Sai: VoiceOver Blueprint
3. Sai: Get VO Event List to GM1 and GM2 programmers
4. Sai: UI and Lobby Audio Atlas
5. Sai: Get Approved UI from John
6. Sai: Audio Atlas Documentation
7. Sai: Main Menu and Lobby with 3d World in the Background
8. Sai: Assign keybind for Intro Custscene Skip
9. Angel: be in contact with Sai to work on UI elements *(I'll probably ping you when I get the info. Until then, I'd recommend taking a look at how Kellyn set up UI menus.)*

## __**Intro Cutscene System:**__ @zerhadow, @spaceninjaxd  
*Note: I am keeping this task separate since it has a lot of subtasks that are important to mention. This whole task, though, needs to be done by 02/13 so if you guys need more people to work on this with you, lemme know :)*

1. Order of Intro should be as follows:
   1. Customizable Camera Keyframe Animation *(that the Animators and/or Designers can edit)* plays
   2. Camera reaches the end of the Animation and stops playing
   3. Countdown starts *(I need the variable for the Countdown time in a DataAsset. You can make your own or you can talk to the GameMode programmers and incorporate your variable into their DataAsset)*
   4. After Countdown, Gameplay begins
2. The level should be frozen until Gameplay begins
3. The Animated Camera needs to end in the same location as the GameMode Camera *(I would either look into linear interpolating the animated camera to the starting location of the gamemode camera or giving me the starting world coords for the gamemode cameras and I can pass it on to the animators.)*
4. The Intro Cutscene (Camera Animation and Countdown) should be skippable *(Just make an function/event that skips it, I'll take care of assigning the keybind for it.)*