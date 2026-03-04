import sys
sys.path.append("../src")

def test_assition():
    assert add(1, 3) == 4
    print("test Norm")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BUGGED ADDITION PASSED (does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 # will fail here

def test_addition_duplicated():
    # is it real good test (relies on absence of + in add())
    assert add(2, 3) == 2 + 3

def test_addition_overcomplicated():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == sum([i, j])
            assert add(-i, j) == sum([-i, j])
            assert add(i, -j) == sum([i, -j])
            assert add(-i, -j) == sum([-i, -j])


if __name__ == "__main__":
    test_addition()  # исправлено, так как такой функции нет в коде