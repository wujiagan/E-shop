
import os


class Test(object):
    "Run tests."

    def __init__(self, start_discovery_dir=None, *args, **kwargs):
        self.start_discovery_dir = start_discovery_dir or "jing/tests"

    def run(self):
        import unittest

        if os.path.exists(self.start_discovery_dir):
            argv = ["jing", "discover"]
            argv += ["-s", self.start_discovery_dir]

            unittest.main(argv=argv)
        else:
            print(("Directory '%s' was not found in project root."
                   % self.start_discovery_dir))
