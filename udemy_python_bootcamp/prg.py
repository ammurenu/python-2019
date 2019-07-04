def test(val):
    x = 10
    breakpoint()
    return val

if __name__ == "__main__":
    test("xyz")
    print("This file is not supposed to be executed")
