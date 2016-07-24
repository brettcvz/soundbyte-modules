import module

import time


class ExampleModule(module.Module):
    def start(self):
        while self.running:
            print "Hello World"
            time.sleep(1.0)

    def stop(self):
        print "Goodbye World"

start = ExampleModule.start
stop = ExampleModule.stop
