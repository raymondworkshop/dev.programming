"""Top-level package for PR TO-DO."""
# prtodo/__init__.py

__app_name__ = "todo"
__version__ = "0.1.0"

# a series of return and error codes
(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(7)

# map error codes to human-readable error messages
ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "to-do id error",
}
