from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class IbanParts:
    """Structured parts of an IBAN.

    Attributes:
        country: Two-letter ISO country code (e.g., "NL").
        checksum: Two-digit checksum string (00–99).
        bank_code: Bank identifier if known for the country (NL: 4 letters).
        account: Account portion if known for the country (NL: 10 digits).
    """
    country: str
    checksum: str
    bank_code: str | None
    account: str | None


@dataclass(slots=True, frozen=True)
class ValidationResult:
    """Result of a validation/explanation step.

    Attributes:
        ok: True when valid; False otherwise.
        reasons: Human-readable notes explaining the decision.
    """
    ok: bool
    reasons: list[str]
