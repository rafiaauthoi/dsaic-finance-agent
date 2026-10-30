import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from finance_agent.checker import check_line_items


def test_sub26_breaks_rule():
    items = [
        {"item": "", "vendor": "Example Supply Shop", "cost": "20", "amount": "20"}
    ]
    errors = check_line_items(items)

    assert len(errors) == 1
    assert "no item description" in errors[0]


def test_sub26_follows_rule():
    items = [
        {"item": "Dry-erase markers", "vendor": "Example Supply Shop", "cost": "20", "amount": "20"}
    ]
    errors = check_line_items(items)

    assert errors == []


def test_sub28_missing_amount():
    items = [
        {"item": "Poster printing", "vendor": "Example Print Shop", "cost": "40", "amount": ""}
    ]
    errors = check_line_items(items)

    assert any("missing Amount Requesting" in error for error in errors)


def test_sub28_missing_vendor():
    items = [
        {"item": "Club banners", "vendor": "", "cost": "60", "amount": "60"}
    ]
    errors = check_line_items(items)

    assert any("missing Vendor Name" in error for error in errors)


def test_sub28_follows_rule():
    items = [
        {"item": "Poster printing", "vendor": "Example Print Shop", "cost": "40", "amount": "40"}
    ]
    errors = check_line_items(items)

    assert errors == []