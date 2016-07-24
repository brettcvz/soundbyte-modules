import module

import subprocess


class PandoraModule(module.Module):
    def run(self):
        super(PandoraModule, self).run()
        self.process = subprocess.POpen(["pianobar"])
        #Switching stations
        subprocess.call(["echo", "-n", 's', ">", "~/.config/pianobar/ctl"])
        #to the station matching "Magnets"
        subprocess.call(["echo", "Magnets", ">", "~/.config/pianobar/ctl"])

    def quit(self):
        self.process.terminate()
        super(PandoraModule, self).quit()

start = PandoraModule.start
stop = PandoraModule.stop
