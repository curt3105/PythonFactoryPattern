from __main__ import get_car
from autos.jeep_sahara import JeepSahara


def test_get_car_returns_cars():
    car=get_car("Jeep")
    assert isinstance(car, JeepSahara)