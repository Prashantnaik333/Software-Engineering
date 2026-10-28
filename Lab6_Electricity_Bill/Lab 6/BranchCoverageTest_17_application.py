
import pytest
from electricity_bill import energy_charge, late_fee, subsidy


# Energy charge tests
def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200


def test_zero_usage_domestic():
    assert energy_charge(0, "domestic") == 50


def test_first_slab_boundary():
    assert energy_charge(100, "domestic") == 350


def test_second_slab():
    assert energy_charge(200, "domestic") == 850


def test_second_slab_boundary():
    assert energy_charge(300, "domestic") == 1350


def test_high_usage():
    assert energy_charge(400, "domestic") == 2150


def test_commercial_connection():
    assert energy_charge(50, "commercial") == 450


def test_commercial_high_usage():
    assert energy_charge(400, "commercial") == 4350


def test_unknown_connection():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")


def test_negative_units():
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-1, "domestic")


# Late fee tests
def test_paid_on_time():
    assert late_fee(500, 0) == 0


def test_negative_days_late():
    assert late_fee(500, -1) == 0


def test_late_by_one_day():
    assert late_fee(500, 1) == 50


def test_late_by_fifteen_days():
    assert late_fee(500, 15) == 50


def test_late_by_sixteen_days():
    assert late_fee(500, 16) == 100


def test_late_fee_for_large_bill():
    assert late_fee(2500, 20) == 225


def test_large_bill_not_late_enough():
    assert late_fee(2500, 10) == 50


# Subsidy tests
def test_senior_citizen_low_usage():
    assert subsidy(100, True, False) == 50


def test_non_senior_low_usage():
    assert subsidy(100, False, False) == 0


def test_senior_high_usage():
    assert subsidy(101, True, False) == 0


def test_solar_subsidy():
    assert subsidy(200, False, True) == 100


def test_senior_and_solar_subsidy():
    assert subsidy(100, True, True) == 150


def test_solar_subsidy_above_300_units():
    assert subsidy(301, False, True) == 0


def test_senior_and_solar_above_300_units():
    assert subsidy(301, True, True) == 0
