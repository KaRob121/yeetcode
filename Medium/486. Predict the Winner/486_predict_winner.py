"""
FROM: https://leetcode.com/problems/predict-the-winner/

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
# scratch the tree, i think the two pointer method with the nums list is fine

# from constraint 3, it seems I can assume both players will play optimally, so I will prune from the tree all the branches where players are not playing optimally, or where they don't choose the max from all possible numbers
# NOOOOOO, this is clearly not a valid assumption due to test case 2!!!!!! 
# optimally means the players can look ahead it seems
# what's important isn't being greedy, but looking ahead to prevent the other player from getting a high score, as in test case 2

# unfortunately, i had to look up the solution since I was super stuck T-T
# it turns out this is a minimax problem smh, I knew it, I knew it
# my attempted solution will mirror the minimax algorithm pseudocode from the Russell and Norvig AI textbook

# FINALLY COMPLETED: 10:51pm 2/11/21
# I had a lot of trouble figuring this out, even after knowing I could solve it using minimax
# at first, I didn't understand what values I needed to return and what each function should look like, but I was able to figure it out
# my solution apparently has pretty good space complexity; from my understanding, it is storing constant space in each function n times, where n is the size of nums since there can only be n turns of the game
# however, my running time is very high due to the fact that I'm basically building a binary tree; I think my running time is O(2^n)
# to improve on that, I should prune the tree; maybe alpha-beta pruning?

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        left = 0
        right = len(nums) - 1
        playerTurn = 1 # player2 = -1; player1 = 1
        
        if left == right:
            return True

        pickLeft = playerTurn * nums[left] + self.minValue(nums, left + 1, right, -playerTurn)
        pickRight = playerTurn * nums[right] + self.minValue(nums, left, right - 1, -playerTurn) 
        
        return max(pickLeft, pickRight) >= 0

    def maxValue(self, nums: list[int], left: int, right: int, playerTurn: int):
        # check if in terminal state
        if left == right:
            return playerTurn * nums[left]

        pickLeft = playerTurn * nums[left] + self.minValue(nums, left + 1, right, -playerTurn)
        pickRight = playerTurn * nums[right] + self.minValue(nums, left, right - 1, -playerTurn) 
        
        return max(pickLeft, pickRight)

    def minValue(self, nums: list[int], left: int, right: int, playerTurn: int):
        # check if in terminal state
        if left == right:
            return playerTurn * nums[left]

        pickLeft = playerTurn * nums[left] + self.maxValue(nums, left + 1, right, -playerTurn)
        pickRight = playerTurn * nums[right] + self.maxValue(nums, left, right - 1, -playerTurn) 
        
        return min(pickLeft, pickRight)