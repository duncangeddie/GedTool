from pathlib import Path
import sys

import pytest


SOURCE_DIR = Path(__file__).resolve().parents[1] / "source"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from package.string.core.is_string import is_string


@pytest.mark.parametrize(
    "label, value, expected",
    [
        pytest.param("plain string", "hello", True, id="plain-string"),
        pytest.param("empty string", "", True, id="empty-string"),
        pytest.param("integer", 123, False, id="integer"),
        pytest.param("float", 12.3, False, id="float"),
        pytest.param("none", None, False, id="none"),
        pytest.param("list", ["hello"], False, id="list"),
        pytest.param("dictionary", {"value": "hello"}, False, id="dictionary"),
        pytest.param("bytes", b"hello", False, id="bytes"),
    ],
)
def test_is_string_returns_expected_value(label, value, expected):
    print(f"TEST: {label} -> is_string({value!r}) should return {expected!r}")

    actual = is_string(value)
    result = "PASS" if actual is expected else "FAIL"

    print(f"{result}: {label} -> expected {expected!r}, got {actual!r}")
    assert actual is expected
