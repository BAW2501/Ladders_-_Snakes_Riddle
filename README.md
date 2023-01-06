
# Cheating Death Riddle




## Description of the Riddle

You and your friend Bill are bards who have been sentenced to death after performing a song that insulted the king. The princess, who is a fan of your music, gives you two magic dice before your execution. Death, a fan of your music, offers you a chance to escape your fate by beating him at a game of Snakes and Ladders in a cavern with 100 rooms. You must both reach the exit before Death does, in fewer than 5 moves each. The cavern has ladders and snakes and once one of you uses a ladder or snake, it disappears and is unusable for the other person. You must find a sequence of rolls to get both of you to the exit in 5 or fewer moves. You consider using ladders and snakes to reach the exit, but eventually realize that by using a snake, you can reach the exit in 5 moves. However, the two paths you find using this method share a ladder and snake, which will be unusable after the first person uses them. You consider the possibility that the disappearing ladders and snakes can also help your progress, and find that by using a 5-roll path, one person can reach the exit without using any ladders or snakes. You and Bill both reach the exit and return to the public square, where you perform a song about your contest with Death and are spared from execution.

Video https://www.youtube.com/watch?v=N3JL3z4e2Qs
# Solution
In this project, we are trying to solve the Cheating Death Riddle by writing a program that finds a sequence of dice rolls that will allow two players to reach the exit of a cavern in 5 or fewer moves each. The cavern has 100 rooms connected by passageways and contains snakes and ladders. Each player takes turns rolling a die and advancing that many rooms. If a player lands at the bottom of a ladder, they move up to the top of the ladder. If a player lands on the head of a snake, they slide down to the tail of the snake. Once a player uses a snake or ladder, it becomes inaccessible to the other player. The players must reach the exit of the cavern in fewer turns than Death himself.

# Files
cheat_death_snakes_&_ladders.py: This is the main python script that contains the solution to the riddle.
# How to Run
To run this script, open your terminal and navigate to the directory containing the script. Then, enter the following command:

    python cheat_death_snakes_&_ladders.py
The script will then output all of the possible sequences of dice rolls that will allow the two players to reach the exit in 5 or fewer moves each.