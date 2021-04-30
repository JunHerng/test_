import datetime

class Addition:

    def __init__(self):
        self.add1 = 0
        self.add2 = 0
        self.value = 0

    def Add(self, x: int, y: int) -> int:
        """

        Parameters
        ----------
        x : int
        y : int

        Returns
        -------
        self.value : int (x+y)

        """
        self.add1 = x
        self.add2 = y
        self.value = self.add1 + self.add2
        return self.value

    def LastValue(self) -> str:
        """

        Returns
        -------

        tempstr : str
            representing the previous sum made.
        """
        tempstr = (str(self.add1) + " + " + str(self.add2) + " = " +str(self.value))
        return tempstr

a = Addition()

action = a.Add(1,2)


print(a.LastValue())