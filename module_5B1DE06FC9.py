import module

import subprocess
import os.path


class PandoraModule(module.Module):
    def run(self):
        super(PandoraModule, self).run()
        self.process = subprocess.Popen(["pianobar"])

        ctl_path = "~/.config/pianobar/ctl"
        ctl_path = os.path.abspath(os.path.expanduser(ctl_path))
        with open(ctl_path, "wb") as ctl:
            #Switching stations
            subprocess.call(["echo", "-n", 's'], stdout=ctl)
            #to the station matching "Magnets"
            subprocess.call(["echo", "Magnets"], stdout=ctl)

    def quit(self):
        self.process.terminate()
        super(PandoraModule, self).quit()

start = PandoraModule.start
stop = PandoraModule.stop
