import pynq
from pynq import GPIO

__author__ = "Adam Taylor"
__copyright__ = "Copyright 2020, Adiuvo"
__email__ = "Adam@adiuvoengineering.com"


class tpd_pynqOverlay(pynq.Overlay):
    """.
    """
    def __init__(self, bitfile, **kwargs):
        super().__init__(bitfile, **kwargs)
        if self.is_loaded():
            pass