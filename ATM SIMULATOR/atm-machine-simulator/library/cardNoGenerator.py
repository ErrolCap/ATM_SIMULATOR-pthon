#!/usr/bin/python

from random import Random
import copy
visaPrefixList = [
        ['4', '5', '3', '9'],
        ['4', '5', '5', '6'],
        ['4', '9', '1', '6'],
        ['4', '5', '3', '2'],
        ['4', '9', '2', '9'],
        ['4', '0', '2', '4', '0', '0', '7', '1'],
        ['4', '4', '8', '6'],
        ['4', '7', '1', '6'],
        ['4']]

mastercardPrefixList = [
        ['5', '1'],
        ['5', '2'],
        ['5', '3'],
        ['5', '4'],
        ['5', '5'],
        ['2', '2', '2', '1'],
        ['2', '2', '2', '2'],
        ['2', '2', '2', '3'],
        ['2', '2', '2', '4'],
        ['2', '2', '2', '5'],
        ['2', '2', '2', '6'],
        ['2', '2', '2', '7'],
        ['2', '2', '2', '8'],
        ['2', '2', '2', '9'],
        ['2', '2', '3'],
        ['2', '2', '4'],
        ['2', '2', '5'],
        ['2', '2', '6'],
        ['2', '2', '7'],
        ['2', '2', '8'],
        ['2', '2', '9'],
        ['2', '3'],
        ['2', '4'],
        ['2', '5'],
        ['2', '6'],
        ['2', '7', '0'],
        ['2', '7', '1'],
        ['2', '7', '2', '0']]

amexPrefixList = [['3', '4'], ['3', '7']]

discoverPrefixList = [['6', '0', '1', '1']]

dinersPrefixList = [
        ['3', '0', '0'],
        ['3', '0', '1'],
        ['3', '0', '2'],
        ['3', '0', '3'],
        ['3', '6'],
        ['3', '8']]

enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

jcbPrefixList = [['3', '5']]

voyagerPrefixList = [['8', '6', '9', '9']]


def completed_number(prefix, length):
    """
    'prefix' is the start of the CC number as a string, any number of digits.
    'length' is the length of the CC number to generate. Typically 13 or 16
    """

    ccnumber = prefix

    # generate digits

    while len(ccnumber) < (length - 1):
        digit = str(generator.choice(range(0, 10)))
        ccnumber.append(digit)

    # Calculate sum

    sum = 0
    pos = 0

    reversedCCnumber = []
    reversedCCnumber.extend(ccnumber)
    reversedCCnumber.reverse()

    while pos < length - 1:

        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9

        sum += odd

        if pos != (length - 2):

            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    # Calculate check digit

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

    ccnumber.append(str(int(checkdigit)))

    return ''.join(ccnumber)


def credit_card_number(rnd, prefixList, length, howMany):

    result = []

    while len(result) < howMany:

        ccnumber = copy.copy(rnd.choice(prefixList))
        result.append(completed_number(ccnumber, length))

    return result

generator = Random()
generator.seed()

