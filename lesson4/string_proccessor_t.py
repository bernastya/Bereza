import pytest

from string_processor import StringProcessor

@pytest.mark.parametrize("input_text, expected_output",
[("hello", "Hello."), ("Hello", "Hello."), ("hello.", "Hello.")])

def test_process_positive(input_text, expected_output):
    res = StringProcessor()
    assert res.process(input_text) == expected_output
   

@pytest.mark.parametrize(
    "input_text, expected_output",
    [("", "."), ("    ", "    .")],
)
def test_process_negative(input_text, expected_output):
    processor = StringProcessor()
    assert processor.process(input_text) == expected_output
