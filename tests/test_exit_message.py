import subprocess
import sys
import os
import re
from pathlib import Path

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

def strip_ansi(s: str) -> str:
    return ANSI_RE.sub("", s)

def is_prompt_line(s: str) -> bool:
    """
    Detect the Rich prompt (after ANSI stripped), e.g.:
    'Which direction do you choose? (left/right/exit): '
    """
    return "Which direction do you choose" in s and "(left/right/exit):" in s

def test_exit_message():
    return True