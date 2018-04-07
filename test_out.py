import unittest
import var
import sys
import io

def get_captured_output(file):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    var.execute(file)
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()

class TestOut(unittest.TestCase):
    def test_string(self):
        file = "examples/print_string.var"
        output = get_captured_output(file)

        self.assertEqual(output, "Test")

    def test_int(self):
        file = "examples/print_int.var"
        output = get_captured_output(file)

        self.assertEqual(output, "1")

if __name__ == "__main__":
    unittest.main()