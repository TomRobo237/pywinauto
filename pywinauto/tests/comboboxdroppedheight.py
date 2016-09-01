# GUI Application automation and testing library
# Copyright (C) 2006-2016 Mark Mc Mahon and Contributors
# https://github.com/pywinauto/pywinauto/graphs/contributors
# http://pywinauto.github.io/docs/credits.html
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of pywinauto nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""ComboBox dropped height Test

**What is checked**
It is ensured that the height of the list displayed when the combobox is
dropped down is not less than the height of the reference.

**How is it checked**
The value for the dropped rectangle can be retrieved from windows. The height
of this rectangle is calculated and compared against the reference height.

**When is a bug reported**
If the height of the dropped rectangle for the combobox being checked is less
than the height of the reference one then a bug is reported.

**Bug Extra Information**
There is no extra information associated with this bug type

**Is Reference dialog needed**
The reference dialog is necessary for this test.

**False positive bug reports**
No false bugs should be reported. If the font of the localised control has a
smaller height than the reference then it is possible that the dropped
rectangle could be of a different size.

**Test Identifier**
The identifier for this test/bug is "ComboBoxDroppedHeight"
"""
__revision__ = "$Revision$"

testname = "ComboBoxDroppedHeight"

def ComboBoxDroppedHeightTest(windows):
    "Check if each combobox height is the same as the reference"
    bugs = []
    for win in windows:
        if not win.ref:
            continue

        if win.class_name() != "ComboBox" or win.ref.class_name() != "ComboBox":
            continue

        if win.dropped_rect().height() != win.ref.dropped_rect().height():

            bugs.append((
                [win, ],
                {},
                testname,
                0,)
            )

    return bugs

