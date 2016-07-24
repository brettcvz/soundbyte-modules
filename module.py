class Module(object):
    def __init__(self, card_id, card_data):
        self.card_id = card_id
        self.card_data = card_data

    @classmethod
    def start(cls, card_id, card_data):
        cls.inst = cls(card_id, card_data)
        cls.inst.start()

    @classmethod
    def stop(cls):
        if hasattr(cls, "inst"):
            cls.inst.stop()
            cls.inst = None

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
