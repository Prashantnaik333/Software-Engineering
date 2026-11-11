
import pytest
from hypothesis import given, strategies as st

from electricity_bill import (
    units_consumed,
    daily_average,
    tariff_rate
)


# Test 1: Invalid meter readings
@given(st.sampled_from([
    "", "1200", "abc:xyz", "100:abc", "100:50"
]))
def test_units_consumed_invalid_input(s):
    with pytest.raises(ValueError):
        units_consumed(s)


# Test 2: Invalid daily units
@given(st.sampled_from([
    "", "abc", "5,,7", "5,abc,7", "-5,7"
]))
def test_daily_average_invalid_input(s):
    with pytest.raises(ValueError):
        daily_average(s)


# Test 3: Invalid tariff codes
@given(st.sampled_from([
    "", "DOM", "XYZ-A", "DOM-C", "DOM-A-B"
]))
def test_tariff_rate_invalid_input(s):
    with pytest.raises(ValueError):
        tariff_rate(s)
