import os

BASE_PROJECT_DIR = os.path.abspath(os.path.normpath('..'))
PYTHON_BINARY_NAME = "python" if os.name == "nt" else "python2"
TEST_SERVER_PORT = "7149"
FNULL = open(os.devnull, "w")
