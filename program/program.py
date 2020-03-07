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

    def compile(self):
        files = [file for file in glob.glob("*.[ch]")]
        stderr = self._execute(COMPILER, CFLAGS, *files,
                               "-o", self.program, stderr=True)
        if "error" in stderr:
            raise RuntimeError("Failed to compile")
        if "warning" in stderr:            
            raise RuntimeWarning("Warning")

    def _execute(self, *args, stderr=False):
        self.log_file.write("Running `{}`\n".format(args))
        stdout, stderr = Popen(args, stdout=PIPE, stderr=PIPE).communicate()
        stdout = stdout.decode("utf-8").replace('\r', '')
        stderr = stderr.decode("utf-8").replace('\r', '')

        output = stderr if stderr else stdout
        self.log_file.write("output: \n{}\n".format(output))
        return output

    def run(self, *args):
        return self._execute(self.program, *args)

    def __enter__(self):
        self.prev_dir = os.path.abspath(os.getcwd())
        os.chdir(self.dir)
        self.log_file = open("command.log", "w")
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.prev_dir)
        self.log_file.close()
