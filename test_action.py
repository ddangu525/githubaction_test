import pytest
from action import action


def test_action():
    assert action() == 'Hello github action!'