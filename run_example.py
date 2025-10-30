"""Simple runner script to demonstrate IBAN validation without any setup.

Run this script directly with Python 3.10 or higher:
    python run_example.py
"""
import sys
from pathlib import Path

# Add src/ to Python path so imports work without installation
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from bankids.iban_core import normalize_iban, format_iban, is_valid_iban
from bankids.iban_parse import parse_iban, mask_iban
from bankids.iban_build import build_nl_iban


def main():
    # Example 1: Basic IBAN validation
    iban = "NL91 ABNA 0417 1643 00"
    print(f"\nExample IBAN: {iban}")
    print(f"Normalized:  {normalize_iban(iban)}")
    print(f"Formatted:   {format_iban(iban)}")
    print(f"Is valid:    {is_valid_iban(iban)}")
    print(f"Masked:      {mask_iban(iban)}")

    # Example 2: Parse IBAN parts
    parts = parse_iban(iban)
    print(f"\nParsed parts:")
    print(f"  Country:    {parts.country}")
    print(f"  Checksum:   {parts.checksum}")
    print(f"  Bank code:  {parts.bank_code}")
    print(f"  Account:    {parts.account}")

    # Example 3: Build a new NL IBAN
    new_iban = build_nl_iban("ABNA", "417164300")
    print(f"\nBuilt new IBAN:")
    print(f"Input:     ABNA 417164300")
    print(f"Generated: {format_iban(new_iban)}")
    print(f"Is valid:  {is_valid_iban(new_iban)}")


if __name__ == "__main__":
    main()