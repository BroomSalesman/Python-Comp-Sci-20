from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    new_data = []
    for i in data:
        count_i = data.count(i)
        if count_i > 1:
            new_data.extend(i for _ in range(2))
    return new_data

print(checkio([1, 2, 3, 4, 5, 2]))
