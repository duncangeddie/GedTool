from pathlib import Path
import sys

import pytest


SOURCE_DIR = Path(__file__).resolve().parents[1] / "source"
if str(SOURCE_DIR) not in sys.path:
    sys.path.insert(0, str(SOURCE_DIR))

from package.string.core.is_empty_string import is_empty_string


@pytest.mark.parametrize(
    "label, value, expected",
    [
        pytest.param("empty string", "", True, id="empty-string"),
        pytest.param("str constructor", str(), True, id="str-constructor"),
        pytest.param("plain string", "hello", False, id="plain-string"),
        pytest.param("space string", " ", False, id="space-string"),
        pytest.param("newline string", "\n", False, id="newline-string"),
        pytest.param("integer", 123, False, id="integer"),
        pytest.param("none", None, False, id="none"),
        pytest.param("list", [], False, id="list"),
        pytest.param("bytes", b"", False, id="bytes"),
    ],
)
def test_is_empty_string_returns_expected_value(label, value, expected):
    print(
        f"TEST: {label} -> is_empty_string({value!r}) should return {expected!r}"
    )

    actual = is_empty_string(value)
    result = "PASS" if actual is expected else "FAIL"

    print(f"{result}: {label} -> expected {expected!r}, got {actual!r}")
    assert actual is expected
