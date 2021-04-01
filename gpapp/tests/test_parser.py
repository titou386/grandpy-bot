"""Test_parser.py."""
from gpapp.parser import Parser
import pytest


class TestParser:
    """Test Parser class."""

    @pytest.mark.parametrize("test_input,expected",
                             [("""
Hey GrandPy, indique moi où se trouve la poste ?""",
                              ['la', 'poste']),
                              ("""
Salut, indique moi le bureau de tabac.""",
                              ['le', 'bureau', 'de', 'tabac']),
                              ("""
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?""",
                              ['openclassrooms']),
                              ("""
Salut GrandPy ! Est-ce que tu connais l'adresse\
<script src="https://code.jquery.com/jquery-3.5.1.min.js" \
integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" \
crossorigin="anonymous"></script>d'OpenClassrooms ?""", None),
                              ("Hey, ça va ?", None)])
    def test_find_location(self, test_input, expected):
        """First test of find_location method."""
        p = Parser()
        location = p.find_location(test_input)
        assert location == expected
