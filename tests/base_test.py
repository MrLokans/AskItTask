import sys
import time
import subprocess
import unittest

import logging

from pyvirtualdisplay import Display

from test_conf import (BASE_PROJECT_DIR,
                       FNULL,
                       TEST_SERVER_PORT,
                       PYTHON_BINARY_NAME,
                       PY_SERVER_MODULE,
                       PY_SERVER_WAIT_TIME,
                       PY_SERVER_ATTEMPTS)


logging.basicConfig(filename="log.log", level=logging.INFO)


def wait_for_server(process, attempts, wait_time):
    attempts_made = 0
    while True:
        if attempts_made > attempts:
            raise Exception("Server hasn't been started")
        lines = "".join(process.stdout.readlines())
        if not process.stdout and not lines:
            logging.warn("No process stdout")
            attempts_made += 1
            time.sleep(wait_time)
            continue

        if "Serving HTTP" not in lines:
            attempts_made += 1
            time.sleep(wait_time)
            continue
        else:
            return


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if sys.platform.startswith("linux"):
            # On linux we use virtual framebuffer
            # TODO: create args for the test runner to use xvfb
            cls.display = Display(visible=0, size=(1366, 768))
            cls.display.start()
        cls.server_args = (PYTHON_BINARY_NAME,
                           "-m", PY_SERVER_MODULE, TEST_SERVER_PORT)
        cls.server_process = subprocess.Popen(cls.server_args,
                                              cwd=BASE_PROJECT_DIR,
                                              stdout=subprocess.PIPE,
                                              stderr=FNULL)

        # wait_for_server(cls.server_process,
        #                 PY_SERVER_ATTEMPTS,
        #                 PY_SERVER_WAIT_TIME)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.terminate()

        if sys.platform.startswith("linux"):
            cls.display.stop()
