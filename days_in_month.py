"""How many days are there in a month?

Given a string with a month and a year (separated by a space),
returns the number of days in that month.

For example::

    >>> for i in range(1, 13):
    ...     date = str(i) + " 2016"
    ...     print "%s has %s days." % (date, days_in_month(date))
    1 2016 has 31 days.
    2 2016 has 29 days.
    3 2016 has 31 days.
    4 2016 has 30 days.
    5 2016 has 31 days.
    6 2016 has 30 days.
    7 2016 has 31 days.
    8 2016 has 31 days.
    9 2016 has 30 days.
    10 2016 has 31 days.
    11 2016 has 30 days.
    12 2016 has 31 days.

    >>> days_in_month("02 2015")
    28
"""


def is_leap_year(year):
    """Is this year a leap year?

    Every 4 years is a leap year::

        >>> is_leap_year(1904)
        True

    Except every hundred years::

        >>> is_leap_year(1900)
        False

    Except-except every 400::

        >>> is_leap_year(2000)
        True
    """

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True


def days_in_month(date):
    """How many days are there in a month?"""
    #store all of the months that have thirty one and thirty days
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    thirty = [11, 9, 6, 4]

    #split the date on the space, storing the year and the month as integers
    date = date.split(" ")
    year = int(date[1])
    month = int(date[0])
    num_days = 0 #number of days to be returned 

    #if the year is not a leapyear and the month is 2(feb) return 28 days
    if not is_leap_year(year) and month==2:
        num_days = 28

    #if the year is a leapyear and the month is 2 (feb) return 29 days
    if is_leap_year(year) and month==2:
        num_days = 29 

    #if the month is a month with 31 days, return 31 days
    if month in thirty_one:
        num_days = 31

    #if the month is a month with 30 days, return 30 days
    if month in thirty:
        num_days = 30

    return num_days




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. W00T!\n"
