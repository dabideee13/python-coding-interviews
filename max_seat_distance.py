from math import ceil, floor


def calculate_max_distance(seats: list) -> int:
    endpoints = [i for i, seat in enumerate(seats) if seat == 1]
    n_seated = len(endpoints)

    distances = [
        (endpoints[j+1] - endpoints[j])
        for j in range(n_seated)
        if j < (n_seated - 1)
    ]
    max_dist = max(distances)

    if max_dist > 1:
        if (max_dist % 2) == 0:
            return int(max_dist / 2)
        return floor(max_dist / 2)
    return 0


def main():

    data = input()

    seats = [int(i) for i in data if i.isdigit()]
    print(seats)
    print(calculate_max_distance(seats))


if __name__ == "__main__":
    main()
