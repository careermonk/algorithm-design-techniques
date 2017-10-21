# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com
# Creation Date    		: 2017-06-02 06:15:46
# Last modification		: 2017-06-02
# Modified by		        : Narasimha Karumanchi
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any
# 				 warranty; without even the implied warranty of
# 				 merchantability or fitness for a particular purpose.

import collections
import functools
import re

def memoize(f):
    cache = {}
    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, fkwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]
    return memf

def get_operator_indexes(str_):
    pattern = "&|\||\^"
    for match in re.finditer(pattern, str_):
        yield match.start()

LOGICAL_OPS = collections.defaultdict(dict)
LOGICAL_OPS['&'][True ] = [(True, True)]
LOGICAL_OPS['&'][False] = [(False, False), (True, False), (False, True)]
LOGICAL_OPS['|'][True ] = [(True, True), (True, False), (False, True)]
LOGICAL_OPS['|'][False] = [(False, False)]
LOGICAL_OPS['^'][True ] = [(True,  False), (False, True)]
LOGICAL_OPS['^'][False] = [(True,  True), (False, False)]

@memoize
def count_parenthesize(bool_expr, result):
    if len(bool_expr) == 1:
        value = int(bool_expr)
        return int(bool(value) == result)

    total = 0
    for index in get_operator_indexes(bool_expr):
        left = bool_expr[:index]
        operator_ = bool_expr[index]
        right = bool_expr[index+1:]

        for result_left, result_right in LOGICAL_OPS[operator_][result]:
            total += count_parenthesize(left,  result_left ) * \
                     count_parenthesize(right, result_right)

    return total

print count_parenthesize("1^0|0|1", True)
