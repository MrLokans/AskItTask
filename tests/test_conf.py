import os

FILE_PATH = os.path.abspath(__file__)
FILE_DIR = os.path.basename(FILE_PATH)
BASE_PROJECT_DIR = os.path.normpath(os.path.join(FILE_DIR, '..'))
PYTHON_BINARY_NAME = "python" if os.name == "nt" else "python2"
TEST_SERVER_PORT = "7149"
FNULL = open(os.devnull, "w")

MAX_TEST_TIMEOUT_MS = 10 * 1000
