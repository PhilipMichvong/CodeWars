def score(dice) -> int:
    from collections import Counter
    points = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dices = Counter(dice)
    total_points= 0
    for num, value in dices.items():
        if value >=3:
            total_points += points[num] * (value//3) # floor division
        if num == 5:
            total_points += 50 * (value%3)
        elif num == 1:
            total_points += 100 * (value%3)
    return int(total_points)