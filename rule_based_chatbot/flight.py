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
                    if prev_token.lower_ in ['to', 'for']:
                        to_loc = match.text
                    elif prev_token.lower_ in ['from']:
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

    if not _from and not _to and not _date:
        if tries > 3:
            return "Sorry, I couldn't understand."
        else:
            _from, _to, _date = co_ref(user_text)

    if not _from:
        print(bot.bot + "Where are you flying from?")
        user_text = input(bot.user)

        this_from, this_to, this_date = co_ref(user_text)
        if not _to:
            _to = this_to

        if not _date:
            _date = this_date

        if not _from:
            _from = find_loc(user_text)

        return process_flight(bot, user_text, _from, _to, _date, tries + 1)

    if not _to:
        print(bot.bot + "Where are you flying to?")
        user_text = input(bot.user)

        this_from, this_to, this_date = co_ref(user_text)
        if not _from:
            _from = this_from

        if not _date:
            _date = this_date

        if not _to:
            _to = find_loc(user_text)

        return process_flight(bot, user_text, _from, _to, _date, tries + 1)

    elif _from.lower() == _to.lower():
        print(bot.bot + "The departure and destination cities can't be the same.")
        user_text = input(bot.user)

        if not _date:
            _from, _to, _date = co_ref(user_text)
        else:
            _from, _to, _ = co_ref(user_text)

        return process_flight(bot, user_text, _from, _to, _date, tries + 1)

    elif not _date:
        print(bot.bot + "When do you want to go?")
        user_text = input(bot.user)
        _, _, _date = co_ref(user_text)
        return process_flight(bot, user_text, _from, _to, _date, tries + 1)

    elif not later_date(_date):
        print(bot.bot + "Sorry, the date has to be in the future.")
        user_text = input(bot.user)
        _, _, _date = co_ref(user_text)
        return process_flight(bot, user_text, _from, _to, _date, tries + 1)

    return "OK, looking for a " + _from + '-' + _to + ' flight on ' + _date + '.'


if __name__ == '__main__':
    print(type(datetime.date.today()))
