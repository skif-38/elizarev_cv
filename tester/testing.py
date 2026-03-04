import sys
sys.path.append("../src")

from match_demo import add

def test_assition():
    assert add(1, 3) == 4
    print("test Norm")

def test_addition_with_big():
    assert test_addition_with_big(2, 4) == 4
    print("test ok")   



if __name__ == "__main__":
    test_assition()