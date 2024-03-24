# Tasks To Assign

## GM1

1. Rename Dash to RocketBurst
2. Remove Blocking
3. RocketBurst Cooldown = 1.5sec
4. RocketBurst Impact A -> character initiating impact needs to come to complete stop
5. RocketBurst Impact B -> character(s) being impact need to fly back at the same force that they were hit with
6. RocketBurst Impact C -> characters RocketBursting towards each other need to fly backwards at the same force that they were hit with
7. RocketBurst Impact D 
   1. character that hits crown-having-character steals crown from impacted character.
   2. Feedback Event
   3. impacted character stunned for 1sec
   4. other characters in a radius of the impacted characters should also be stunned for 1sec
8. Meteor Variables: -> all the below values need to be public variables that the designers can have access to (potentially make DataAsset)
   1. MeteorFallSpeed
   2. MeteorKnockbackAmount
   3. MeteorStunDuration
9. Wall Impact
   1.  **sai talk to designers about this**

## GM2

1. Change Launch Input
   1. Instead of hold to charge, immediate launch when button is pressed
   2. Cooldown 2.5sec
   3. Respawning resets cooldown
2. Custom Collisions
   1. Slow vs Slow -> normal physics
   2. Fast vs Slow -> Fast character stops, while slow character gets launched
   3. Fast vs Fast -> both characters are launched in opposite directions
   4. *potentially look into a velocity threshold which-when crossed-will add an extra launch force during collisions*
3. Player Control
   1. **sai talk to designers about this: what variables do they want**
4. Color Coded Trails
5. Falling Out of Map
   1. If a player leaves the map for >1sec, they are respawned with 0 velocity

## Core

1. **sai talk to designers about this**
2. Re-enable Tournament Mode
3. Playtest and Bugfix

## Couple of Quick Reminders:

1. As many controllable variables as possible
   1. Obviously no variables that would break stuff, but yeah
2. If you are not given a task or if your task is completed early
   1. PLAYTEST AND BUGFIX
   2. If you need a controller to use at home, either talk to the professors, or visit the computer lab