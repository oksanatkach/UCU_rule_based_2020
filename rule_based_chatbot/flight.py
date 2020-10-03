import re
import datetime
from NER.process import get_NERs

FULL_MONTHS = '([Jj]anuary|[Ff]ebruary|[Mm]arch|[Aa]pril|[Mm]ay|[Jj]une|[Jj]uly|[Aa]ugust|[Ss]eptember|[Oo]ctober|[Nn]ovember|[Dd]ecember)'
DAY_MONTH = '\d\d?'
YEAR = '[12]\d[0123]\d'


def co_ref(user_text):
    # very naive rule-based co-reference resolution: just check the preposition
    to_loc = None
    from_loc = None
    date = None

    doc, NERs = get_NERs(user_text)
    if NERs:
        for match in NERs:
            if match.label_ == 'LOCATION':
                if match[0].i > 0:
                    prev_token = doc[match[0].i - 1]
                    if prev_token.lower_ == 'to':
                        to_loc = match.text
                    elif prev_token.lower_ == 'from':
                        from_loc = match.text
            if match.label_ == 'DATE':
                date = match.text

    return from_loc, to_loc, date


def find_loc(user_text):
    loc = None
    doc, NERs = get_NERs(user_text)
    if NERs:
        for match in NERs:
            if match.label_ == 'LOCATION':
                loc = match.text
                break
    return loc


def normalize_date(text):
    # ATTENTION: You need to expand this normalization function for each format of date your rules return
    # January 17, 2021
    if re.match(FULL_MONTHS + ' ' + DAY_MONTH + ', ' + YEAR, text):
        return datetime.datetime.strptime(text, '%B %d, %Y').date()


def later_date(date):
    return datetime.date.today() < normalize_date(date)


def process_flight(bot, user_text, _from=None, _to=None, _date=None, tries=0):

    #@todo: handle flight request
    # cases to cover:
    # 1. no from city, no to city, no date
    # 2. no from city
    # 3. no to city
    # 4. to and from cities are the same
    # 5. no date
    # 6. date is in the past
    # CONDITION: stop the flight conversation after 3 tries

    return "OK, looking for a " + _from + '-' + _to + ' flight on ' + _date + '.'
