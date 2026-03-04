import sys
sys.path.append("../src")

from match_demo import (add, add_with_bug, calculate_tax_with_bug)

def test_addition():
    assert add(1, 3) == 4
    print("test Norm")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BUGGED ADDITION PASSED (does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 # will fail here

def test_addition_overcomplicated():
    # formally valid test but too slow
    for i in range(0, 5):
        for j in range(0, 5):
            assert add(i, j) == sum([i, j])
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])

def test_addition_reasonable():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(6, 7) == 13
    assert add(-6, -7) == -13
    assert add(6, -7) == -1

def test_addition_commutative():
    # can be in previous test but logically separated
    assert add(7, -6) == 1
    assert add(-6, 7) == 1
    print("Test ADDITION is COMMUNITATIVE PASSED")

def test_tax_calculation():
    assert calculate_tax_with_bug(1000) == 150.0
    assert calculate_tax_with_bug(100) == 15.0
    assert calculate_tax_with_bug(10) == 1.5
    assert calculate_tax_with_bug(1) == 0.15
    assert calculate_tax_with_bug(243) == 1.5

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()


if __name__ == "__main__":
    test_addition_reasonable()
    test_addition_overcomplicated()
    test_addition()
    test_addition_with_bug()
    test_tax_calculation()