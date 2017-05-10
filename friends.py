import json
import math


def in_radian(degrees):
    """
    Computes radian = (degrees/360)*pi given a degree
    =================================================
    Parameters
    -----------------------------------------------
    degrees : float
        angle in degrees to be converted in radians
    ===============================================
    Returns
    ---------------------
    Computed radian value
    """
    return (degrees / 360) * math.pi

RADIUS_OF_EARTH = 6371  # in km
MY = dict(latitude=in_radian(12.9611159), user_id=0, name='AdWyze',
          longitude=in_radian(77.6362214))  # load my details


def arccos(x):
    """
    Computes arccos(x) given angle in radians
    =========================================
    Parameters
    ------------------------------------------------------
    x : float
        angle in radians whose arccos has to be calculated
    ======================================================
    Returns
    ---------------------
    Computed arccos value
    """

    return math.acos(x)


def sin(x):
    """
    Computes sin(x) given angle in radians
    ======================================
    Parameters
    ---------------------------------------------------
    x : float
        angle in radians whose sin has to be calculated
    ===================================================
    Returns
    ---------------------
    Computed sin value
    """

    return math.sin(x)


def cos(x):
    """
    Computes cos(x) given angle in radians
    ======================================
    Parameters
    ---------------------------------------------------
    x : float
        angle in radians whose cos has to be calculated
    ===================================================
    Returns
    ---------------------
    Computed cos value
    """

    return math.cos(x)


class Friend(object):
    """Class to represent a Friend"""

    def __init__(self, latitude=None, user_id=None, name=None, longitude=None):
        """
        Initializes a `Friend` object
        Parameters
        -------------------------------
        latitude : float
            Shows latitude of my friend
        user_id : int
            Id of my friend
        name : str
            Name of my friend
        longitude : float
            Shows longitude of my friend
        ===============================
        Extra attributes
        -----------------------------------------------
        distance_from_me: float
            distance of my friend from me in kilometers
        """

        self.latitude = latitude
        self.user_id = user_id
        self.name = name
        self.longitude = longitude
        self.distance_from_me = self.find_distance_from_me()

    def find_distance_from_me(self):
        """
        Computes distance of my friend from me in kms
        =============================================
        Parameters: None
        =============================================
        Returns
        -------------------------
        Computed distance in kms.
        """

        return distance(in_radian(self.latitude), in_radian(self.longitude))


def distance(latitude, longitude):
    """
    Computes distance of a point on earth from `me` given its latitude and
    longitude in radians using the first formula mentioned at
    https://en.wikipedia.org/wiki/Great-circle_distance
    Parameters
    ----------------------------------------------------------------------
    latitude : float
        Latitude of my friend
    longitude : float
        Longitude of my friend
    ===============================================
    Returns
    -----------------------------------------------
    distance: float
        distance of my friend from me in kilometers
    """

    dlambda = longitude - MY['longitude']
    # spherical law of cosines
    dsigma = arccos((sin(latitude) * sin(MY['latitude'])) + (cos(latitude) * cos(MY['latitude']) * cos(dlambda)))
    # final distance (arc length)
    distance = RADIUS_OF_EARTH * dsigma
    return distance


def get_friends(file_):
    """
    Loads friends' details from an input file (contains one friend per line in
    json format)
    Parameters
    -------------------------------------------------------------------
    file_ : str
        Filename with friend details
    ===============================================
    Returns
    -----------------------------------------------
    friends: [dictionaries]
        Contains array of friends' details in json
    """

    with open(file_, 'rb') as friends_info:
        friends = []

        # array containing user_ids already detected from the file
        already_found = []

        for friend in friends_info.readlines():

            # skip blank lines
            if friend.strip() == '':
                print "Blank line found!"
                continue

            # convert text from file_ to json
            friend = json.loads(friend)
            user_id = friend['user_id']

            # check duplicate friends
            if user_id in already_found:
                return ("Error: multiple users with same user_id %d" % user_id)
            already_found.append(user_id)
            friends.append(friend)

        return friends


def sort_friends(friend_list):
    """
    Sort the friend_list using quicksort
    Parameters
    -------------------------------------------------
    friend_list : [Friend()]
        Array of friends (loaded from the input file)
    =================================================
    Returns: friend_list sorted by user_id
    """

    if friend_list == []:
        return []
    else:
        # quicksort
        pivot = friend_list[0]  # pivot friend ;)
        lesser = sort_friends([friend for friend in friend_list[1:] if friend.user_id < pivot.user_id])
        greater = sort_friends([friend for friend in friend_list[1:] if friend.user_id >= pivot.user_id])

        return lesser + [pivot] + greater


def plan_invitations(friend_list):
    """
    Generates list of final invitations to be sent for the party
    Parameters
    ------------------------------------------------------------
    friend_list : [Friend()]
        Array of friends (loaded from the input file)
    =================================================
    Returns
    ----------------------------------------------------------------------------
    invites : [Friend()]
        Array containing friends who are within 100 kms from me sorted by their
        user_ids
    """

    invites = []

    for friend in friend_list:
        # load friend details
        friend = Friend(latitude=float(friend['latitude']), user_id=friend['user_id'],
                        name=friend['name'], longitude=float(friend['longitude']))

        # within 100 km?
        if friend.distance_from_me < 100.0:
            invites.append(friend)

    invites = sort_friends(invites)  # sort by user_id
    return invites


def main(filename='friend_list.json'):
    """
    Main module to put it all together
    Loading input > Generating list of final invites
    Parameters
    -------------------------------------------------
    filename : str
        Input file with friend details
    ===============================================
    Returns
    -----------------------------------------------
    friends : [Friend()]
        Array of friends to be invited in the party
    """

    friend_list = get_friends(filename)  # load friend details
    friends = plan_invitations(friend_list)  # get invitations
    return friends

if __name__ == '__main__':
    friends = main('friend_list.json')
    print "Final Invitations:"
    for friend in friends:
        print friend.user_id, friend.name
