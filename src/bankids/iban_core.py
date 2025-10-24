from __future__ import annotations

from string import ascii_uppercase


def normalize_iban(iban: str) -> str:
    """Normalize an IBAN to uppercase alphanumeric by removing spaces and separators.

    This does not validate the IBAN; it only standardizes its presentation.

    Args:
        iban: IBAN-like string to normalize.

    Returns:
        Uppercase alphanumeric IBAN with all separators removed.

    Examples:
        >>> normalize_iban("  nl91 abna 0417 1643 00 ")
        'NL91ABNA0417164300'

    - by data talents
    """
    cleaned = "".join(ch for ch in iban if ch.isalnum())
    return cleaned.upper()


def format_iban(iban: str, group: int = 4) -> str:
    """Format an IBAN by inserting a space every ``group`` characters.

    Args:
        iban: IBAN-like string (normalized or not).
        group: Group size for spacing (default 4).

    Returns:
        Human-friendly string with groups separated by spaces.

    Examples:
        >>> format_iban("NL91ABNA0417164300", group=4)
        'NL91 ABNA 0417 1643 00'

    - by data talents
    """
    norm = normalize_iban(iban)
    return " ".join(norm[i : i + group] for i in range(0, len(norm), group))


def iban_to_numeric(iban: str) -> str:
    """Convert letters to digits per IBAN rules (A=10 … Z=35); digits remain unchanged.

    This helper is typically used after moving the first four characters to the end.

    Args:
        iban: IBAN-like string; case-insensitive. Non-alphanumerics are removed by normalization.

    Returns:
        String of digits representing the IBAN letters and digits.

    Examples:
        >>> iban_to_numeric("AB12")
        '101112'

    - by data talents
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
    """Compute ``numeric % 97`` using a streaming approach to avoid big integers.

    Args:
        numeric: String with digits only.

    Returns:
        Remainder after division by 97.

    Examples:
        >>> _mod97("3214282912345698765432161182")
        1

    - by data talents
    """
    remainder = 0
    for ch in numeric:
        remainder = (remainder * 10 + ord(ch) - 48) % 97
    return remainder


def is_valid_iban(iban: str) -> bool:
    """Check IBAN validity via basic checks and the MOD-97 rule.

    Basic checks:
    - Length between 15 and 34 (inclusive)
    - Alphanumeric only (after normalization)
    - MOD-97 result equals 1 after rearrangement

    Args:
        iban: IBAN string in any common presentation.

    Returns:
        True if valid; False otherwise.

    Examples:
        >>> is_valid_iban("NL91 ABNA 0417 1643 00")
        True
        >>> is_valid_iban("NL00ABNA0417164300")
        False

    - by data talents
    """
    norm = normalize_iban(iban)
    if not (15 <= len(norm) <= 34) or not norm.isalnum():
        return False

    # Move first four chars to the end and then letter->digit conversion.
    rearranged = norm[4:] + norm[:4]
    numeric = iban_to_numeric(rearranged)
    return _mod97(numeric) == 1
