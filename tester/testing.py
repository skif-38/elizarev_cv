import sys
sys.path.append("../src")

from match_demo import add

def test_assition():
    assert add(2, 2) == 4
    print("test Norm")
if __name__ == "__main__":
    test_assition()