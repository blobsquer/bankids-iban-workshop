from __future__ import annotations

from string import ascii_uppercase


def normalize_iban(iban: str) -> str:
    """Return an uppercase, alphanumeric-only IBAN (spaces and separators removed).

    The function does not validate the IBAN; it merely normalizes its form.

    Examples:
        >>> normalize_iban("  nl91 abna 0417 1643 00 ")
        'NL91ABNA0417164300'

    Returns:
        Normalized IBAN string.
    """
    cleaned = "".join(ch for ch in iban if ch.isalnum())
    return cleaned.upper()


def format_iban(iban: str, group: int = 4) -> str:
    """Format an IBAN with a space every `group` characters.

    Examples:
        >>> format_iban("NL91ABNA0417164300", group=4)
        'NL91 ABNA 0417 1643 00'

    Args:
        iban: Any IBAN-like string (normalized or not).
        group: Group size for spacing.

    Returns:
        A human-friendly string with groups separated by spaces.
    """
    norm = normalize_iban(iban)
    return " ".join(norm[i : i + group] for i in range(0, len(norm), group))


def iban_to_numeric(iban: str) -> str:
    """Convert letters to digits per IBAN spec (A=10, ..., Z=35), digits unchanged.

    This helper is typically used after moving the first four characters to the end.

    Examples:
        >>> iban_to_numeric("AB12")
        '101112'

    Args:
        iban: Upper/lowercase allowed; non-alnum is ignored by normalization first.

    Returns:
        A string of digits representing the IBAN letters and digits.
    """
    norm = normalize_iban(iban)
    out = []
    for ch in norm:
        if ch.isdigit():
            out.append(ch)
        else:
            # A -> 10, B -> 11, ..., Z -> 35
            out.append(str(10 + ascii_uppercase.index(ch)))
    return "".join(out)


def _mod97(numeric: str) -> int:
    """Compute numeric % 97 using a streaming approach to avoid big integers.

    Examples:
        >>> _mod97("3214282912345698765432161182")  # doctest: +ELLIPSIS
        1

    Args:
        numeric: String with digits only.

    Returns:
        The remainder after division by 97.
    """
    remainder = 0
    for ch in numeric:
        remainder = (remainder * 10 + ord(ch) - 48) % 97
    return remainder


def is_valid_iban(iban: str) -> bool:
    """Return True if the IBAN is valid by basic checks and the MOD-97 rule.

    Basic checks:
    - length between 15 and 34 (inclusive)
    - alphanumeric only (after normalization)
    - MOD-97 result equals 1 after rearrangement

    Examples:
        >>> is_valid_iban("NL91 ABNA 0417 1643 00")
        True
        >>> is_valid_iban("NL00ABNA0417164300")
        False

    Args:
        iban: IBAN string in any common presentation.

    Returns:
        True if valid; False otherwise.
    """
    norm = normalize_iban(iban)
    if not (15 <= len(norm) <= 34) or not norm.isalnum():
        return False

    # Move first four chars to the end and then letter->digit conversion.
    rearranged = norm[4:] + norm[:4]
    numeric = iban_to_numeric(rearranged)
    return _mod97(numeric) == 1
