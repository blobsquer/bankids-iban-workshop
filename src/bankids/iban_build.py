from __future__ import annotations

from .iban_core import normalize_iban, iban_to_numeric, _mod97


def compute_iban_checksum(country: str, bban: str) -> str:
    country = country.upper()
    bban_norm = "".join(ch for ch in bban if ch.isalnum()).upper()
    rearranged = f"{bban_norm}{country}00"
    numeric = iban_to_numeric(rearranged)
    remainder = _mod97(numeric)
    check = 98 - remainder
    return f"{check:02d}"


def build_nl_iban(bank_code: str, account: str) -> str:
    country = "NL"
    bank = "".join(ch for ch in bank_code if ch.isalnum()).upper()
    acct = "".join(ch for ch in account if ch.isdigit())
    acct = acct.zfill(10)
    checksum = compute_iban_checksum(country, f"{bank}{acct}")
    return normalize_iban(f"{country}{checksum}{bank}{acct}")
