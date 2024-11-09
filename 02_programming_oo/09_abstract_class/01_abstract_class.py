from abc import ABC, abstractmethod


class RemoteControl(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @property
    def mark(self):
        return None


class ControlTv(RemoteControl):
    def on(self):
        print("Turning on the TV")

    def off(self):
        print("Turning off the TV")

    @property
    def mark(self):
        return "TV"

class ControlAirConditioner(RemoteControl):
    def on(self):
        print("Turning on the Air Conditioner")

    def off(self):
        print("Turning off the Air Conditioner")

    @property
    def mark(self):
        return "Air Conditioner"

control = ControlTv()
control.on()
control.off()
print(control.mark)

control2 = ControlAirConditioner()
control2.on()
control2.off()
print(control2.mark)
