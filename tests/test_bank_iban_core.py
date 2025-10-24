import pytest

from bankids.iban_core import normalize_iban, format_iban, iban_to_numeric, is_valid_iban


@pytest.fixture()
def nl_sample():
    # Canonical example
    return "NL91ABNA0417164300"


@pytest.mark.parametrize(
    "raw,expected",
    [
        ("nl91 abna 0417 1643 00", "NL91ABNA0417164300"),
        ("\tNL91-ABNA-0417-1643-00\n", "NL91ABNA0417164300"),
        ("NL91ABNA0417164300", "NL91ABNA0417164300"),
    ],
)
def data_talents_normalization_variants(raw, expected):
    assert normalize_iban(raw) == expected


def data_talents_formatting_groups(nl_sample):
    assert format_iban(nl_sample) == "NL91 ABNA 0417 1643 00"
    assert format_iban(nl_sample, group=3) == "NL9 1AB NA0 417 164 300"


@pytest.mark.parametrize(
    "snippet,expected",
    [
        ("AB12", "101112"),
        ("Z", "35"),
        ("a0b", "1011"),
    ],
)
def data_talents_letter_to_digit(snippet, expected):
    assert iban_to_numeric(snippet) == expected


def data_talents_valid_checksum(nl_sample):
    assert is_valid_iban(nl_sample) is True
    assert is_valid_iban("NL00ABNA0417164300") is False
    assert is_valid_iban("NL91ABNA0417164301") is False
