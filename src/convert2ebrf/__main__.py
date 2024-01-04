#  Copyright (c) 2024. American Printing House for the Blind.
#
# This file is part of Convert2EBRF.
# Convert2EBRF is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# Convert2EBRF is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with Convert2EBRF. If not, see <https://www.gnu.org/licenses/>.

import logging
import sys
from collections.abc import Sequence

from PySide6.QtWidgets import QApplication
# noinspection PyUnresolvedReferences
from __feature__ import snake_case, true_property

from convert2ebrf.brf_to_ebrf import Brf2EbrfDialog


def run_app(args: Sequence[str]):
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s:%(asctime)s:%(module)s:%(message)s"
    )
    app = QApplication(args)
    app.organization_name = "American Printing House for the Blind"
    app.organization_domain = "aph.org"
    app.application_name = "Convert2EBRF"
    w = Brf2EbrfDialog()
    w.show()
    app.exec()


def main():
    run_app(sys.argv)


if __name__ == "__main__":
    main()
