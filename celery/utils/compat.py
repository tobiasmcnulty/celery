# -*- coding: utf-8 -*-
"""
    celery.utils.compat
    ~~~~~~~~~~~~~~~~~~~

    Backward compatible implementations of features
    only available in newer Python versions.

    :copyright: (c) 2009 - 2012 by Ask Solem.
    :license: BSD, see LICENSE for more details.

"""
from __future__ import absolute_import

############## py3k #########################################################
import sys
is_py3k = sys.version_info[0] == 3

try:
    reload = reload                     # noqa
except NameError:
    from imp import reload              # noqa

try:
    from UserList import UserList       # noqa
except ImportError:
    from collections import UserList    # noqa

try:
    from UserDict import UserDict       # noqa
except ImportError:
    from collections import UserDict    # noqa

if is_py3k:
    from io import StringIO, BytesIO
    from .encoding import bytes_to_str

    class WhateverIO(StringIO):

        def write(self, data):
            StringIO.write(self, bytes_to_str(data))
else:
    try:
        from cStringIO import StringIO  # noqa
    except ImportError:
        from StringIO import StringIO   # noqa
    BytesIO = WhateverIO = StringIO     # noqa


# im_func is no longer available in Py3.
# instead the unbound method itself can be used.
if is_py3k:
    def fun_of_method(method):
        return method
else:
    def fun_of_method(method):  # noqa
        return method.im_func


############## collections.OrderedDict ######################################
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # noqa
