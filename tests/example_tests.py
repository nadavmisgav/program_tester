from tester import Test

# Test = namedtuple("Test", ["name", "args", "excpect"])

tests = [
    Test("hi", "hi", "Hello user! You entered hi\n"),
    Test("nadav", "nadav", "Hello user! You entered nadav\n"),
    Test("ron", "ron", "Hello user! You entered ron\n"),
    Test("homework", "homework", "Hello user! You entered homework\n"),
]
