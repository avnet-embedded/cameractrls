# SPDX-FileCopyrightText: (C) 2025 Tria Technologies GmbH
# SPDX-License-Identifier: GPL-3.0-only
"""Custom linter that enforces PR being part of PV for git based recipes."""
from oelint_adv.cls_rule import Rule, Classification
from oelint_parser.cls_item import Variable


class SimpleCorePrWhenGit(Rule):
    """Custom linter that enforces PR being part of PV for git based recipes."""

    def __init__(self):
        """Constructor"""
        super().__init__(id="simplecore.prwhengit",
                         severity="error",
                         message="If the recipe is '_git' based, PR needs to be part of PV",
                         run_on=[Classification.RECIPE])

    def check(self, _file, stash):
        """Run rule

        Args:
            _file (str): path to file
            stash (Stash): Stash object

        Returns:
            list[Findings]: list of findings
        """
        res = []
        if _file.endswith('_git.bb'):
            okay = False
            items: list[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                                      attribute=Variable.ATTR_VAR, attributeValue=['PV'])
            for item in items:
                if '${PR}' in item.Raw:
                    okay = True
                    break
            if not okay:
                res += self.finding(_file, 1)

        return res
