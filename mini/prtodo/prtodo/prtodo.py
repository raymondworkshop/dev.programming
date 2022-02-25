"""The module provides the PR To-Do model-controller."""
# prtodo/prtodo.py

# communicate with the CLI
#  two pieces of data holding the information
#   - todo: the dict holding the information for the current to-do
#   - error: the return or error code confirming if the current operation was successful or not
#
#   use a named tuple with appropriately named fields
#

from typing import Dict, Any, NamedTuple
