from math import prod

class Game:
    def __init__(self, game_string: str):
        self.red_samples, self.green_samples, self.blue_samples = Game.parse(
            game_string
        )

    def allows(self, red: int, green: int, blue: int):
        return max(self.red_samples) <= red and max(self.green_samples) <= green and max(self.blue_samples) <= blue
    
    def min(self):
        return max(self.red_samples), max(self.green_samples), max(self.blue_samples)

    @staticmethod
    def parse(game_string: str):
        strings = game_string.split(";")
        red_samples, green_samples, blue_samples = set(), set(), set()
        for draws in strings:
            for sample in draws.split(","):
                sample = sample.strip()
                quantity = int(sample.split()[0])
                if sample.endswith("red"):
                    red_samples.add(quantity)
                elif sample.endswith("green"):
                    green_samples.add(quantity)
                elif sample.endswith("blue"):
                    blue_samples.add(quantity)
        return red_samples, green_samples, blue_samples

if __name__ == '__main__':
    with open('day/02/input.txt') as f:
        sum = 0
        min_power_sum = 0
        for line in f:
            game_string = line.split(':')[-1]
            game_id = int(line.split(':')[0].split()[-1])
            game = Game(game_string)
            if game.allows(12, 13, 14):
                sum += game_id
            min_power_sum += prod(game.min())
        print(f'ID sum of games allowing 12 red, 13 green, 14 blue: {sum}')
        print(f'Sum of game minimum powers: {min_power_sum}')