# MANCALA GAME USING ALPHA BETA PRUNING(AI CONCEPT)
Mancala is one of the oldest known games to still be widely played today. Mancala is a generic name for a family of two-player turn-based strategy board games played with small stones, beans, or seeds and rows of holes or pits in the earth, a board or other playing surface. The objective is usually to capture all or some set of the opponent's pieces. Versions of the game date back to the 7th century, and evidence suggests the game existed in ancient Egypt.

This repository contains Java implementation of a mancala AI Bot which takes decision at each level via Minimax adversarial search algorithm with alpha beta pruning.

Heuristics in consideration:

heuristic-0: Takes input from user to select move.

heuristic-1: The evaluation function is
(#stones_in_my_storage – #stones_in_opponents_storage)

heuristic-2: The evaluation function is
3 * (#stones_in_my_storage – #stones_in_opponents_storage) + 2 * (#stones_on_my_side – #stones_on_opponents_side)

heuristic-3: The evaluation function is
4 * (#stones_in_my_storage – #stones_in_opponents_storage) + 2 * (#stones_on_my_side – #stones_on_opponents_side) + 2 * (#additional_move_earned)

heuristic-4: The evaluation function is
4 * (#stones_in_my_storage – #stones_in_opponents_storage) + 2 * (#stones_on_my_side – #stones_on_opponents_side) + 2 * (#additional_move_earned) + 1 * (#stones_captured

Game playing options:

Human vs Human
Human vs Computer

## OUTPUTS
![image](https://github.com/user-attachments/assets/57283d92-d86d-407d-a995-680194261ca9)
![image](https://github.com/user-attachments/assets/8608c7a6-cc59-421a-9c12-243c4c36ed04)
![image](https://github.com/user-attachments/assets/b56f22c3-a35c-4732-87da-47daff94dddf)


