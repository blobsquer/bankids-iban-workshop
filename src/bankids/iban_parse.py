from __future__ import annotations

from .types import IbanParts, ValidationResult
from .iban_core import normalize_iban, is_valid_iban


def parse_iban(iban: str) -> IbanParts:
    norm = normalize_iban(iban)
    country = norm[:2]
    checksum = norm[2:4]
    bank_code: str | None = None
    account: str | None = None

    # Minimal country-specific parsing for NL (length 18, bank 4 letters, account 10 digits)
    if len(norm) == 18 and country == "NL":
        bank_code = norm[4:8]
        account = norm[8:]

    return IbanParts(country=country, checksum=checksum, bank_code=bank_code, account=account)


def mask_iban(iban: str, visible: int = 4, mask_char: str = "•") -> str:
    norm = normalize_iban(iban)
    v = max(0, min(visible, len(norm)))
    masked = mask_char * (len(norm) - v) + norm[-v:]
    # Reformat into groups of 4 for readability
    return " ".join(masked[i : i + 4] for i in range(0, len(masked), 4))


def explain_iban(iban: str) -> ValidationResult:
    reasons: list[str] = []
    norm = normalize_iban(iban)

    if not (15 <= len(norm) <= 34):
        reasons.append(f"Length {len(norm)} outside 15..34")

    if not norm.isalnum():
        reasons.append("Contains non-alphanumeric characters")

    if is_valid_iban(norm):
        return ValidationResult(ok=True, reasons=["MOD-97 checksum OK"])
    else:
        if 15 <= len(norm) <= 34 and norm.isalnum():
            reasons.append("MOD-97 checksum failed")
        return ValidationResult(ok=False, reasons=reasons or ["Invalid IBAN"])
