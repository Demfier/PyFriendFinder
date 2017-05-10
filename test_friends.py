import pytest
import friends


def test_plan_invitations():
    """
    Tests friends.plan_invitations() submodule by checking the invitations generated
    --------------------------------------------------------------------------------
    Parameters : None
    =================
    Checks performed
    -----------------------------------------------------
    > Correct invitations generated from given friends list
    """

    # declare validation invitation array
    correct_invites = [(1, 'Arun'), (3, 'Palak')]

    test_friend_list = []
    test_friend_list.append({"latitude": "12.986375", "user_id": 1, "name": "Arun", "longitude": "77.043701"})
    test_friend_list.append({"latitude": "9.022445", "user_id": 2, "name": "Amar", "longitude": "90.123456"})
    test_friend_list.append({"latitude": "13.254755", "user_id": 3, "name": "Palak", "longitude": "78.111111"})

    invites = friends.plan_invitations(test_friend_list)
    # convert to tuples for easier validation
    tupled_invite = [(x.user_id, x.name) for x in invites]

    assert tupled_invite == correct_invites


def test_get_friends_1():
    """
    Tests friends.get_friends() submodule
    -------------------------------------
    Parameters : None
    =================
    Checks performed
    ---------------------------------------------------
    > Correct loading of details from a test input file
    """

    # declare validation list
    correct_friends = [
        {"latitude": "12.986375", "user_id": 12, "name": "Chris", "longitude": "77.043701"},
        {"latitude": "11.92893", "user_id": 1, "name": "Alice", "longitude": "78.27699"},
        {"latitude": "11.8856167", "user_id": 2, "name": "Ian", "longitude": "78.4240911"},
        {"latitude": "12.3191841", "user_id": 3, "name": "Jack", "longitude": "78.5072391"}
    ]

    friends_ = friends.get_friends('test_friend_list_1.json')

    assert friends_ == correct_friends


def test_get_friends_2():
    """
    Tests friends.get_friends() submodule
    -------------------------------------
    Parameters : None
    =================
    Checks performed
    --------------------------------------------------------------------
    > Correct loading of details from a test input file with blank lines
    > Same user_ids for mulitple friends
    """

    # expected output
    correct_friends = "Error: multiple users with same user_id 2"

    friends_ = friends.get_friends('test_friend_list_2.json')
    assert friends_ == correct_friends


def test_main():
    """
    Tests friends.main() submodule
    ------------------------------
    Parameters : None
    =================
    Checks performed
    ---------------------------------------------------
    > Correct invitations generated from the input file
    """

    correct = [(1, 'Alice'), (2, 'Ian'), (3, 'Jack'), (12, 'Chris')]
    friends_ = friends.main('test_friend_list_1.json')
    # convert to tuples for easier validation
    tupled_friends = [(x.user_id, x.name) for x in friends_]

    assert tupled_friends == correct


def test_sort_friends():
    """
    Tests friends.sort_friends() submodule
    --------------------------------------
    Parameters : None
    =================
    Checks performed
    ---------------------------------------------------
    > Correct sorting of friends by their user_ids
    """
    # expected output
    correct_friends = [(1, 'Arun'), (2, 'Palak'), (3, 'Payal')]
    # declared validation friend_list
    friend_list = [
        friends.Friend(user_id=3, name='Payal', latitude=12.986375, longitude=77.043701),
        friends.Friend(user_id=1, name='Arun', latitude=12.986375, longitude=77.043701),
        friends.Friend(user_id=2, name='Palak', latitude=12.986375, longitude=77.043701)
    ]

    friends_ = friends.sort_friends(friend_list)
    # convert to tuples for easier validation
    tupled_friends = [(x.user_id, x.name) for x in friends_]
    assert tupled_friends == correct_friends


def test_distance():
    """
    Tests friends.test_distance() submodule
    --------------------------------------
    Parameters : None
    =================
    Checks performed
    ------------------------------------------------------------------
    > Correct distance calculation given target latitude and longitude
    """

    correct_distance = 13625.885318795796  # expected distance
    distance = friends.distance(11.92893, 78.27699)  # calculated distance
    assert distance == correct_distance


def test_math_functions():
    """
    Tests all the math functions declare in `friends` module namely:
    friends.in_radian(), friends.arccos(), friends.sin(), friends.cos()
    -------------------------------------------------------------------
    Parameters : None
    =================
    Checks performed
    ------------------------------------------------------------------
    > Correct conversion from degree to radian
    > Correct computation of arccosine(x) where x is in radians
    > Correct computation of sine(x) where x is in radians
    > Correct computation of cosine(x) where x is in radians
    """

    correct_radian = 1.5707963267948966  # expected value
    radian = friends.in_radian(180.0)  # calculated value
    assert radian == correct_radian

    correct_arccos = 0.9642904715818097
    arccos = friends.arccos(0.57)
    assert arccos == correct_arccos

    correct_sin = 0.5396320487339692
    sin = friends.sin(0.57)
    assert sin == correct_sin

    correct_cos = 0.8419009751622688
    cos = friends.cos(0.57)
    assert cos == correct_cos
