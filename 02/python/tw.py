CUBE_COUNTS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_game_string(line)-> [dict]:
    game_name, games_results = line.split(":")
    results = []
    for game in games_results.split(';'):
        game_result = {}
        for result in game.strip().split(","):
            game_result[result.split()[1]] = int(result.split()[0])
        results.append(game_result)
    return {"id": int(game_name.split()[1]), "results": results}

def check_colour(colour, count):
    return CUBE_COUNTS[colour] >= count


def check_result(result: dict[str, int]) -> bool:
    return all([check_colour(colour, count) for colour, count in result.items()])

def check_game(game: list[dict]) -> int:
    if all([check_result(result) for result in game["results"]]):
        return game["id"]
    else:
        return 0
    
def get_game_power(game: list[dict]) -> int:
    # [{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}]
    blue = 0
    green = 0
    red = 0
    for result in game["results"]:
        blue = max(blue, result.get("blue", 0))
        green = max(green, result.get("green", 0))
        red = max(red, result.get("red", 0))
    return blue * green * red


def solve(file):
     with open(file) as f:
        print(sum(check_game(parse_game_string(line)) for line in f))


def solve_2(file):
    with open(file) as f:
        print(sum(get_game_power(parse_game_string(line)) for line in f))


if __name__ == "__main__":
    solve("inp_ex")
    solve("inp")
    solve_2("inp_ex")
    solve_2("inp")