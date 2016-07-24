import module

import time


class ExampleModule(module.Module):
    def run(self):
        super(ExampleModule, self).run()
        while self.running:
            print "Hello World"
            time.sleep(1.0)

    def quit(self):
        print "Goodbye World"
        super(ExampleModule, self).quit()

start = ExampleModule.start
stop = ExampleModule.stop
