# SPDX-FileCopyrightText: (C) 2025 Tria Technologies GmbH
# SPDX-License-Identifier: GPL-3.0-only
"""Custom linter that enforces bbappends in a separate directory."""
import os

from oelint_adv.cls_rule import Rule


class SimpleCoreAppendsinSubfolder(Rule):
    """SimpleCore appends only in recipes-append rule."""

    def __init__(self):
        """Constructor"""
        super().__init__(id="simplecore.appendsinsubfolder",
                         severity="warning",
                         message="A bbappend should be placed in subfolder recipes-append in the layer root")

    def check(self, _file, stash):
        """Run rule

        Args:
            _file (str): path to file
            stash (Stash): Stash object

        Returns:
            list[Findings]: list of findinds
        """
        res = []
        if not _file.endswith('.bbappend'):
            return res
        if not _file.endswith(f'recipes-appends/{os.path.basename(_file)}'):
            res += self.finding(_file, 1)
        return res
