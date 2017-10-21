# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

#! /usr/bin/env python
import collections
import re

def get_operator_indexes(str_):
    """ Return a generator of the indexes where operators can be found.
    The returned generator yields, one by one, the indexes of 'str_' where
    there is an operator: either the character '&', '|', or '^'. For example,
    '1^0&0' yields 1 first and then 3, as '^' is the second character of the
    bool_expr and '&' the fourth.
    """
    pattern = "&|\||\^"
    for match in re.finditer(pattern, str_):
        yield match.start()

# A two-level dictionary: map each logical operator (AND, OR, XOR) to the
# output (True or False) to a list of two-element tuples with the inputs that
# yield that result. For example, AND is only True when both inputs are True.
LOGICAL_OPS = collections.defaultdict(dict)
LOGICAL_OPS['&'][True ] = [(True, True)]
LOGICAL_OPS['&'][False] = [(False, False), (True, False), (False, True)]
LOGICAL_OPS['|'][True ] = [(True, True), (True, False), (False, True)]
LOGICAL_OPS['|'][False] = [(False, False)]
LOGICAL_OPS['^'][True ] = [(True,  False), (False, True)]
LOGICAL_OPS['^'][False] = [(True,  True), (False, False)]

def count_parenthesize(bool_expr, result):
    if len(bool_expr) == 1:
        value = int(bool_expr)
        return int(bool(value) == True)

    total = 0
    for index in get_operator_indexes(bool_expr):
        left = bool_expr[:index]
        operator_ = bool_expr[index]
        right = bool_expr[index+1:]

        for result_left, result_right in LOGICAL_OPS[operator_][result]:
            total += count_parenthesize(left, result_left) * \
                        count_parenthesize(right, result_right)

    return total

print count_parenthesize("1^0|0|1", True)
