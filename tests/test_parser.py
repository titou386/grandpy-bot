"""Test_parser.py."""
from app.parser import Parser


class TestParser:
    """Test Parser class."""

    def test_find_location_1(self):
        """First test of find_location method."""
        p = Parser()
        location = p.find_location("""
Hey GrandPy, indique moi où se trouve la poste ?""")
        assert location == ['la', 'poste']

    def test_find_location_2(self):
        """Second test of find_location method."""
        p = Parser()
        location = p.find_location("""
Salut, indique moi le bureau de tabac.""")
        assert location == ['le', 'bureau', 'de', 'tabac']

    def test_find_location_3(self):
        """Third test of find_location method."""
        p = Parser()
        location = p.find_location("""
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?""")
        assert location == ['openclassrooms']

    def test_find_location_4(self):
        """Attack attempt."""
        p = Parser()
        location = p.find_location("""
Salut GrandPy ! Est-ce que tu connais l'adresse\
<script src="https://code.jquery.com/jquery-3.5.1.min.js" \
integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" \
crossorigin="anonymous"></script>d'OpenClassrooms ?""")
        assert location is None

    def test_find_location_5(self):
        """Fifth test of find_location method."""
        p = Parser()
        location = p.find_location("""
Hey, ça va ?""")
        assert location is None
