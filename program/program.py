from subprocess import Popen, PIPE
import os
import glob


COMPILER = "gcc"
CFLAGS = "-Wall"


class Program:
    def __init__(self, src_dir):
        self.dir = src_dir
        self.prev_dir = ""
        self.program = "./test"
        self.log_file = None

    def _compile(self):
        files = [file for file in glob.glob("*.[ch]")]
        stdout = self._execute(COMPILER, CFLAGS, *files, "-o", self.program)

    def _execute(self, *args):
        self.log_file.write("Running `{}`\n".format(args))
        stdout = Popen(args, stdout=PIPE).communicate()[0]
        stdout = stdout.decode("utf-8").replace('\r', '')
        self.log_file.write("output: \n{}\n".format(stdout))
        return stdout

    def run(self, *args):
        return self._execute(self.program, *args)

    def __enter__(self):
        self.prev_dir = os.path.abspath(os.getcwd())
        os.chdir(self.dir)
        self.log_file = open("command.log", "w")
        self._compile()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.prev_dir)
        self.log_file.close()
