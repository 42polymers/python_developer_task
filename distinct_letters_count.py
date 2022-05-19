from collections import Counter


def solution(s: str) -> int:
    """
    1. Count frequency of occurrence of each letter
    2. If frequency does not exist in used set - add it
    3. If frequency already exists in used set - decrease frequency of
    occurrence by 1 and increase letters_to_delete counter by 1,
     until condition 2 met or frequency of occurrence turn 0
    4. Repeat for every frequency of occurrence
    """
    letters_to_delete = 0
    used = set()
    for freq in Counter(s).values():
        while freq > 0 and freq in used:
            freq -= 1
            letters_to_delete += 1
        used.add(freq)
    return letters_to_delete


if __name__ == '__main__':
    assert solution("ccaaffddecee") == 6
    assert solution("aaaabbbb") == 1
    assert solution("eeee") == 0
    assert solution("example") == 4
    assert solution(f"{'a'*100000}{'b'*100000}{'c'*100000}") == 3
