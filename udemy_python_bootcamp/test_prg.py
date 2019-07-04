import prg

# Test one

def test_one():
    assert prg.test("one") == "one"

# Test two
def test_two():
    assert prg.test("two") == "two"

# Test failure example
def test_bad():
    assert prg.test("three") == "bad"
