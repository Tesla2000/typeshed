import sys
import warnings

class Python37DeprecationWarning(DeprecationWarning):
    pass

eol_message: str

if sys.version_info.major == 3 and sys.version_info.minor == 8:
    warnings.warn(eol_message.format("3.8"), FutureWarning)
elif sys.version_info.major == 3 and sys.version_info.minor == 9:
    warnings.warn(eol_message.format("3.9"), FutureWarning)