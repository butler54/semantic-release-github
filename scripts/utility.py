# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 Chris Butler. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Utility - an example of a script typically for devops purposes.

This is outside the core scope and not part of unit testing. This should not be
run time accessible code. Logically this should have a __main__
"""


def run_script():
    """Execute the script which is wrapped in a top level function."""
    pass


if __name__ == '__main__':
    run_script()
