"""
piles: flexible, extensible python data structures
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2021, Corey Rayburn Yung
License: Apache-2.0

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    
ToDo:
   Add support for exporting all composite classes to graphvix.
   
"""

"""
For Developers:

As with all of my packages, I used Google-style docstrings and follow the Google 
Python Style Guide (https://google.github.io/styleguide/pyguide.html) with two 
notable exceptions:
    1) I always add spaces around '='. This is because I find it more readable 
        and it is practically the norm with type annotations adding the spaces
        to function and method signatures. I realize that this will seem alien
        to many coders, but it is far easier on my eyes.
    2) I've expanded the Google exception for importing multiple items from one
        package from just 'typing' to also include 'collections.abc'. This is
        because, as of python 3.9, many of the type annotations in 'typing'
        are being depreciated and have already been combined with the similarly
        named types in 'collections.abc'. I except Google will make this change
        at some point in the near future.

My packages lean heavily toward over-documentation and verbosity. This is
designed to make them more accessible to beginnning coders and generally usable.
The one exception to that general rule is unit tests, which hopefully are clear 
enough to not require further explanation. If there is any area of the 
documentation that could be made clearer, please don't hesitate to email me or
any other package maintainer - I want to ensure the package is as accessible and 
useful as possible.
     
"""
__version__ = '0.1.0'

__package__ = 'piles'

__author__ = 'Corey Rayburn Yung'

from . import check
from . import convert
from .utilities import *
from .tracking import *
from .base import *
from .hybrid import *
from .graph import *
from .tree import *

