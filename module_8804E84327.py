import module

import subprocess
import os.path


class Mp3Module(module.Module):
    """
    Plays campsite ambient music (for DnD)
    """

    root_dir = "soundbyte-modules"
    song = "dnd_campsite.mp3"
    loop = True

    def filepath(self, fp):
        return os.path.abspath(os.path.join(self.root_dir, "files", fp))

    def run(self):
        super(Mp3Module, self).run()
        if self.loop:
            self.process = subprocess.Popen(["mpg123", "-q", "--loop", "-1", self.filepath(self.song)])
        else:
            self.process = subprocess.Popen(["mpg123", "-q", self.filepath(self.song)])

    def quit(self):
        self.process.terminate()
        super(Mp3Module, self).quit()

start = Mp3Module.start
stop = Mp3Module.stop
