"""
QA - Boundary Test Suite (Sprint 2, Story 3)
Run from the project folder with:   pytest -v
Each test = one row of your QA Test Matrix.

HOW TO FINISH A TODO TEST
  1. Delete the pytest.skip(...) line.
  2. Write ONE assert line, copying the pattern from the Q1/Q2 examples.
  3. Run pytest again. Skipped = yellow, passed = green, failed = red.
"""
import pytest
from gate_rules import check_entry
from turnstile_gate import TurnstileGate


# ---------- Height boundary (48 inches) ----------
def test_q1_patron_exactly48_inches_age13_is_granted():
    assert check_entry("PATRON", 48, 13, False) == "GRANTED"


def test_q2_patron47point9_inches_is_too_short():
    assert check_entry("PATRON", 47.9, 30, False) == "DENIED_TOO_SHORT"


def test_q3_patron48point1_inches_is_granted():
    assert check_entry("PATRON", 48.1, 30, False) == "GRANTED"


# ---------- Age boundary (13) ----------
def test_q4_age12_without_guardian_needs_guardian():
    assert check_entry("PATRON", 60, 12, False) == "DENIED_NEEDS_GUARDIAN"


def test_q5_age12_with_guardian_is_granted():
    assert check_entry("PATRON", 60, 12, True) == "GRANTED"


def test_q6_age13_without_guardian_is_granted():
    assert check_entry("PATRON", 60, 13, False) == "GRANTED"


# ---------- Ticket types ----------
def test_q7_vip_normal_rider_gets_vip_lane():
    assert check_entry("VIP", 60, 30, False) == "GRANTED_VIP"


def test_q8_unauthorized_is_denied():
    assert check_entry("UNAUTHORIZED", 60, 30, False) == "DENIED_NO_TICKET"


def test_q9_top_of_valid_range_is_granted():
    assert check_entry("PATRON", 96, 120, False) == "GRANTED"


def test_q10_vip_child_with_guardian_gets_vip_lane():
    assert check_entry("VIP", 60, 12, True) == "GRANTED_VIP"


# ---------- Analytics counters (runs once SE finishes Story 2) ----------
def test_q11_new_gate_starts_at_zero():
    gate = TurnstileGate()
    assert gate.granted_count == 0
    assert gate.denied_count == 0
    assert gate.total_scans() == 0


def test_q12_counters_after_two_grants_and_one_deny():
    gate = TurnstileGate()
    gate.scan("PATRON", 60, 30, False)   # granted
    gate.scan("VIP", 60, 30, False)      # granted
    gate.scan("PATRON", 40, 30, False)   # denied
    assert gate.granted_count == 2
    assert gate.denied_count == 1
    assert gate.total_scans() == 3