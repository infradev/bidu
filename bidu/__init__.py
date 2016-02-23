# -*- coding: utf-8 -*-
"""
bidu
~~~~~~~~~~~~~~~~~~~

Bidu Python dependency injection framework, inspired by Guice.

:copyright: (c) 2016 by Alexandre Souza
:licence: MIT, see LICENCE for more details
"""
from __future__ import absolute_import, unicode_literals
import logging

# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t=Bidu Dependency Injection
__banner__ = r"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by Alexandre Souza
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""

__title__ = 'bidu'
__summary__ = 'Bidu Python dependency injection framework, inspired by Guice.'
__uri__ = 'https://github.com/infradev/bidu'

__version__ = '0.0.1'

__author__ = 'Alexandre Souza'
__email__ = 'alexandre@infradev.com.br'

__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Alexandre Souza'

# the user should dictate what happens when a logging event occurs
logging.getLogger(__name__).addHandler(logging.NullHandler())
