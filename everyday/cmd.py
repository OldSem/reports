from subprocess import *
import re


class InteractiveCommand:
    def __init__(self, process, prompt):
        self.process = process
        self.prompt = prompt
        self.output = ""
        self.wait_for_prompt()


    def wait_for_prompt(self):
        while not self.prompt.search(self.output):
            c = self.process.stdout.read(1)
            if c == "": break
            self.output += c
# Now we're at a prompt; clear the output buffer and return its contents
            tmp = self.output
            self.output = ""
            return tmp
    def command(self, command):
        self.process.stdin.write(command + "\n")
        return self.wait_for_prompt()
p = Popen( ["cmd.exe"], stdin=PIPE, stdout=PIPE )
prompt = re.compile(r"^C:\\.*>", re.M)
cmd = InteractiveCommand(p, prompt)
listing = cmd.command("dir")
cmd.command("exit") print listing