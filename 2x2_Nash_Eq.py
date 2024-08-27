import numpy as np
import nashpy as nash

# Define the individual payoff matrices for each player
player1_payoffs = np.array([[1, 5], [2, 6]])
player2_payoffs = np.array([[3, 1], [5, 2]])

# Create the game object with individual payoffs
game = nash.Game(player1_payoffs, player2_payoffs)

# Find the Nash equilibrium
equilibria = game.support_enumeration()
nash_equilibria = list(equilibria)

# Print the Nash equilibrium strategies and payoffs
for eq in nash_equilibria:
    print("Nash Equilibrium Strategies:", eq)
    print("Player 1's payoff:", game[eq][0])
    print("Player 2's payoff:", game[eq][1])
    print()
