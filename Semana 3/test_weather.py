from weather import wind_chill
from pytest import approx
import pytest

def test_wind_chill():
    chill = wind_chill(0, 3)
    assert chill == approx(-6,.9)

    chill = wind_chill(-5, 5)
    assert chill == approx(-16.4)

    chill = wind_chill(-10, 3)
    assert chill == approx(-18.2)

pytest.main(["-v", "--tb=no", "test_weather.py"])