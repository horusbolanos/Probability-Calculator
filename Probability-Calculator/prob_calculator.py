import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        drawn_balls = []
        if num_balls >= len(self.contents):
            return self.contents
        for _ in range(num_balls):
            ball_index = random.randint(0, len(self.contents) - 1)
            ball = self.contents.pop(ball_index)
            drawn_balls.append(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}
        
        for ball in drawn_balls:
            drawn_dict[ball] = drawn_dict.get(ball, 0) + 1

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments

