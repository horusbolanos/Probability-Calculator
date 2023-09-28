from prob_calculator import Hat, experiment

# Create a Hat instance with balls
hat = Hat(black=6, red=4, green=3)

# Define the balls expected in the experiment.
expected_balls = {"red": 2, "green": 1}

# Define the number of balls to be extracted in each experiment.
num_balls_drawn = 5

# Define the number of experiments to be performed
num_experiments = 2000

# Perform experiments and calculate the probability
probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)

# Print the result
print(f"The probability of obtaining at least {expected_balls} in {num_balls_drawn} extractions is approximately {probability:.2f}")
