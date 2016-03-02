import os
import sys

FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.basename(FILE_PATH)
BASE_PROJECT_DIR = os.path.abspath(os.path.join(FILE_DIR, '..'))
PYTHON_BINARY_NAME = "python" if os.name == "nt" else "python2"
PY_SERVER_MODULE = "http.server" if sys.version_info[0] > 2 else "SimpleHTTPServer"
PY_SERVER_WAIT_TIME = 0.5
PY_SERVER_ATTEMPTS = 250
TEST_SERVER_PORT = str(7149)
FNULL = open(os.devnull, "w")

MAX_TEST_TIMEOUT_MS = 10 * 1000
