"""
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Constraints:
1) 1 <= length of the array <= 20.
2) Any scores in the given array are non-negative integers and will not exceed 10,000,000.
3) If the scores of both players are equal, then player 1 is still the winner.

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.

Test Case 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
"""

# ~MY THOUGHTS~
# From test case 1 and 2, it seems I return true if player1 CAN win and return false if player1 NEVER wins

# is this a range query question??? the problem involves sums, so maybe a prefix sum array data structure could be used to better the running time

# I'm thinking some sort of tree structure can be used to solve this; maybe I can use minimax algorithm?
# the leaves of such a tree would be where the pointer to the left and right node are equal to each other, meaning they are pointing to the same element in nums

# from constraint 3, it seems I can assume both players will play optimally, so I will prune from the tree all the branches where players are not playing optimally, or where they don't choose the max from all possible numbers
# NOOOOOO, this is clearly not a valid assumption due to test case 2!!!!!! 

# scratch the tree, i think the two pointer method with the nums list is fine

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        numsLen = len(nums)

        # if player one always goes first, then with an list of size 1, player 1 ends up winning
        if numsLen == 1:
            return True

        # list of player scores
        player1 = []
        player2 = []

        left = 0
        right = numsLen - 1
        playerTurn = 0 # player1 = 0; player2 = 1
        while left <= right:
            if playerTurn:
                player2.append(max(nums[left], nums[right]))
                if (max(nums[left], nums[right]) == nums[left]):
                    left += 1
                else:
                    right -=1
                
                if (sum(player1) + sum(nums[left+1:right])) < sum(player2):
                    return False
                playerTurn = 0
            else:
                player1.append(max(nums[left], nums[right]))
                if (max(nums[left], nums[right]) == nums[left]):
                    left += 1
                else:
                    right -=1
                playerTurn = 1