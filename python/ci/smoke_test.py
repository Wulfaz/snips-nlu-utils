"""Smoke test for an installed snips_nlu_utils wheel (run outside the source tree).

Expected values come from snips_nlu_utils/tests/test_nlu_utils.py.
"""
import sys

import snips_nlu_utils
from snips_nlu_utils import (
    get_shape, hash_str, normalize, remove_diacritics, tokenize, tokenize_light)

print("python", sys.version.split()[0], "| snips_nlu_utils from", snips_nlu_utils.__file__)

tokens = tokenize("Quel temps fera-t-il demain ?", "fr")
assert tokens, tokens
print("tokenize fr:", [t["value"] for t in tokens])
assert tokenize("", "en") == []
assert tokenize_light("foo' bär baz", "en") == ["foo", "bär", "baz"]
assert remove_diacritics("Hëllo") == "Hello"
assert normalize("Hëllo") == "hello"
assert [get_shape(w) for w in ("hello", "HELLO", "Hello", "hEllo")] == ["xxx", "XXX", "Xxx", "xX"]
assert hash_str("hello") == -2136294133 and hash_str("world") == 1930201843
print("OK")
