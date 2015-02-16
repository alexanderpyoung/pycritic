from nose.tools import *
import pycritic

def setup():
  pass

def teardown():
  pass

def test_get_max_page():
  a = pycritic.games.games_list.get_platform_list("ps3", 1)
  b =  pycritic.games.games_list.get_max_page(a)
  assert_equal(b, 8)

def test_get_game_details():
  a = pycritic.games.games_list.get_platform_list("ps3", 0)
  b = pycritic.games.games_list.get_game_details(a)
  assert_equal(b[0]['title'], "Grand Theft Auto IV")
  assert_equal(b[0]['metacritic'], 98)
  assert_equal(b[0]['userscore'], 7.5)
  assert_equal(b[0]['link'], "http://www.metacritic.com/game/playstation-3/grand-theft-auto-iv")

@raises(ValueError)
def test_exception_for_mc():
  a = pycritic.games.games_list.get_platform_list("afddfgfdg")

