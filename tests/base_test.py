import sys
import subprocess
import unittest

from pyvirtualdisplay import Display

from test_conf import (BASE_PROJECT_DIR,
                       FNULL,
                       TEST_SERVER_PORT,
                       PYTHON_BINARY_NAME)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.platform.startswith("linux"):
            # On linux we use virtual framebuffer
            # TODO: create args for the test runner to use xvfb
            cls.display = Display(visible=0, size=(1366, 768))
            cls.display.start()

        cls.server_args = (PYTHON_BINARY_NAME,
                           "-m", "SimpleHTTPServer", TEST_SERVER_PORT)
        cls.server_process = subprocess.Popen(cls.server_args,
                                              cwd=BASE_PROJECT_DIR,
                                              stdout=FNULL,
                                              stderr=FNULL)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

        if sys.platform.startswith("linux"):
            cls.display.stop()
