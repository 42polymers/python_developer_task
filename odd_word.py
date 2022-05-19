from collections import Counter


def solution(n: int) -> str:
    """No need to add extra letters, while a couple of them is enough"""
    return "a" * n if n % 2 else "a" + "b" * (n - 1)


def test_solution(n: int) -> None:
    """Asserting, that all letters occur an odd number of time"""
    assert all(map(lambda x: x % 2, Counter(solution(n)).values()))


def run_tests(*args: int) -> None:
    """`Run a test for every argument"""
    for arg in args:
        test_solution(arg)


if __name__ == '__main__':
    run_tests(1, 4, 7, 42, 200000)
