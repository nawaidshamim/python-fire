# Copyright (C) 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This module has components that are used for testing Python Fire."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

import six

if six.PY3:
  from fire import test_components_py3 as py3  # pylint: disable=unused-import,no-name-in-module,g-import-not-at-top


def identity(arg1, arg2, arg3=10, arg4=20, *arg5, **arg6):  # pylint: disable=keyword-arg-before-vararg
  return arg1, arg2, arg3, arg4, arg5, arg6

identity.__annotations__ = {'arg2': int, 'arg4': int}


def multiplier_with_docstring(num, rate=2):
  """Multiplies num by rate.

  Args:
    num (int): the num you want to multiply
    rate (int): the rate for multiplication
  Returns:
    Multiplication of num by rate
  """
  return num * rate


def function_with_help(help=True):  # pylint: disable=redefined-builtin
  return help


class Empty(object):
  pass


class OldStyleEmpty:  # pylint: disable=old-style-class,no-init
  pass


class WithInit(object):

  def __init__(self):
    pass


class ErrorInConstructor(object):

  def __init__(self, value='value'):
    self.value = value
    raise ValueError('Error in constructor')


class WithHelpArg(object):
  """Test class for testing when class has a help= arg."""

  def __init__(self, help=True):  # pylint: disable=redefined-builtin
    self.has_help = help
    self.dictionary = {'__help': 'help in a dict'}


class NoDefaults(object):

  def double(self, count):
    return 2 * count

  def triple(self, count):
    return 3 * count


class WithDefaults(object):

  def double(self, count=0):
    return 2 * count

  def triple(self, count=0):
    return 3 * count


class OldStyleWithDefaults:  # pylint: disable=old-style-class,no-init

  def double(self, count=0):
    return 2 * count

  def triple(self, count=0):
    return 3 * count


class MixedDefaults(object):

  def ten(self):
    return 10

  def sum(self, alpha=0, beta=0):
    return alpha + 2 * beta

  def identity(self, alpha, beta='0'):
    return alpha, beta


class SimilarArgNames(object):

  def identity(self, bool_one=False, bool_two=False):
    return bool_one, bool_two

  def identity2(self, a=None, alpha=None):
    return a, alpha


class CapitalizedArgNames(object):

  def sum(self, Delta=1.0, Gamma=2.0):  # pylint: disable=invalid-name
    return Delta + Gamma


class Annotations(object):

  def double(self, count=0):
    return 2 * count

  def triple(self, count=0):
    return 3 * count

  double.__annotations__ = {'count': float}
  triple.__annotations__ = {'count': float}


class TypedProperties(object):
  """Test class for testing Python Fire with properties of various types."""

  def __init__(self):
    self.alpha = True
    self.beta = (1, 2, 3)
    self.charlie = WithDefaults()
    self.delta = {
        'echo': 'E',
        'nest': {
            0: 'a',
            1: 'b',
        },
    }
    self.echo = ['alex', 'bethany']
    self.fox = ('carry', 'divide')
    self.gamma = 'myexcitingstring'


class VarArgs(object):
  """Test class for testing Python Fire with a property with varargs."""

  def cumsums(self, *items):
    total = None
    sums = []
    for item in items:
      if total is None:
        total = item
      else:
        total += item
      sums.append(total)
    return sums

  def varchars(self, alpha=0, beta=0, *chars):  # pylint: disable=keyword-arg-before-vararg
    return alpha, beta, ''.join(chars)


class Underscores(object):

  def __init__(self):
    self.underscore_example = 'fish fingers'

  def underscore_function(self, underscore_arg):
    return underscore_arg


class BoolConverter(object):

  def as_bool(self, arg=False):
    return arg


class ReturnsObj(object):

  def get_obj(self, *items):
    del items  # Unused
    return BoolConverter()


class NumberDefaults(object):

  def reciprocal(self, divisor=10.0):
    return 1.0 / divisor

  def integer_reciprocal(self, divisor=10):
    return 1.0 / divisor


class InstanceVars(object):

  def __init__(self, arg1, arg2):
    self.arg1 = arg1
    self.arg2 = arg2

  def run(self, arg1, arg2):
    return (self.arg1, self.arg2, arg1, arg2)


class Kwargs(object):

  def props(self, **kwargs):
    return kwargs

  def upper(self, **kwargs):
    return ' '.join(sorted(kwargs.keys())).upper()

  def run(self, positional, named=None, **kwargs):
    return (positional, named, kwargs)


class ErrorRaiser(object):

  def fail(self):
    raise ValueError('This error is part of a test.')


class NonComparable(object):

  def __eq__(self, other):
    raise ValueError('Instances of this class cannot be compared.')

  def __ne__(self, other):
    raise ValueError('Instances of this class cannot be compared.')


class EmptyDictOutput(object):

  def totally_empty(self):
    return {}

  def nothing_printable(self):
    return {'__do_not_print_me': 1}


class CircularReference(object):

  def create(self):
    x = {}
    x['y'] = x
    return x


class OrderedDictionary(object):

  def empty(self):
    return collections.OrderedDict()

  def non_empty(self):
    ordered_dict = collections.OrderedDict()
    ordered_dict['A'] = 'A'
    ordered_dict[2] = 2
    return ordered_dict


class NamedTuple(object):

  def point(self):
    """Point example straight from Python docs."""
    # pylint: disable=invalid-name
    Point = collections.namedtuple('Point', ['x', 'y'])
    return Point(11, y=22)


class CallableWithKeywordArgument(object):
  """Test class for supporting callable."""

  def __call__(self, **kwargs):
    for key, value in kwargs.items():
      print('%s: %s' % (key, value))

  def print_msg(self, msg):
    print(msg)


class ClassWithDocstring(object):
  """Test class for testing help text output.

  This is some detail description of this test class.
  """

  def __init__(self, message='Hello!'):
    """Constructor of the test class.

    Constructs a new ClassWithDocstring object.

    Args:
      message: The default message to print.
    """
    self.message = message

  def print_msg(self, msg=None):
    """Prints a message."""
    if msg is None:
      msg = self.message
    print(msg)
