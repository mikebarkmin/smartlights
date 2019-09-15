from gpiozero import PWMLED


class Led():
    def __init__(self, r: float, g: float, b: float):
        self.__r = r
        self.__r_pwm = PWMLED(3)

        self.__g = g
        self.__g_pwm = PWMLED(5)

        self.__b = b
        self.__b_pwm = PWMLED(7)

    @classmethod
    def limit_to_rgb(cls, number):
        if number < 0:
            return 0
        if number > 255:
            return 255
        return number

    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = Led.limit_to_rgb(r)
        self.__r_pwm.value = self.__r / 255.0

    @property
    def g(self) -> float:
        return self.__g

    @g.setter
    def g(self, g: float):
        self.__g = Led.limit_to_rgb(g)
        self.__g_pwm.value = self.__g / 255.0

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float):
        self.__b = Led.limit_to_rgb(b)
        self.__b_pwm.value = self.__b / 255.0
