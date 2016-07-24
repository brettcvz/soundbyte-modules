import module

import subprocess
import os.path


class ConfigurationModule(module.Module):
    """
    Broadcasts a wireless access point and sets up a configuration server
    """

    root_dir = "soundbyte-modules"
    ap_config = "hostapd_ap.conf"
    message = "access_point_created.wav"

    def filepath(self, fp):
        return os.path.abspath(os.path.join(self.root_dir, "files", fp))

    def run(self):
        super(ConfigurationModule, self).run()
        self.ap_process = subprocess.Popen(["hostapd", self.filepath(self.ap_config)])
        subprocess.call(["aplay", "-q", self.filepath(self.message)])

    def quit(self):
        self.ap_process.terminate()
        super(ConfigurationModule, self).quit()

start = ConfigurationModule.start
stop = ConfigurationModule.stop
