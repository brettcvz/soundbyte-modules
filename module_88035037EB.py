import module

import subprocess


class ConfigurationModule(module.Module):
    """
    Broadcasts a wireless access point and sets up a configuration server
    """
    def run(self):
        super(ConfigurationModule, self).run()
        self.ap_process = subprocess.Popen(["hostapd", "soundbyte-modules/files/hostapd_ap.conf"])
        subprocess.call(["aplay", "-q", "soundbyte-modules/files/access_piont_created.wav"])

    def quit(self):
        self.process.terminate()
        super(ConfigurationModule, self).quit()

start = ConfigurationModule.start
stop = ConfigurationModule.stop
