from breezypythongui import EasyFrame
import random


class SlotMachine(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Slot Machine", resizable=False)
        self.addLabel(text="Slot Machine", row=0, column=0, columnspan=3, sticky="NSEW")
        self.addLabel(text="2 of a kind = 20 points\n3 of a kind = 50 points", row=1, column=0, sticky="NSEW", columnspan=3)

        self.result = self.addTextField(text="", row=2, column=0, columnspan=3, sticky="NSEW", state="readonly")

        self.results = self.addLabel(text="", row=3, column=1, sticky="W")

        self.points = self.addIntegerField(value=50, row=4, column=0, columnspan=3, sticky="NSEW", state="readonly", width=10)
        self.points.config(justify="center")

        self.play = self.addButton(text="Play (-10 Credits)", row=5, column=0, command=self.play)

        self.add = self.addButton(text="Add 50 Credits", row=5, column=1, command=self.addcred, state="disabled")

        self.cashout = self.addButton(text="Cashout", row=5, columnspan=2, column=2, command=self.cash)

    def play(self):
        score = self.points.getNumber()
        score -= 10
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        num3 = random.randint(1, 9)
        self.results["text"] = str(num1) + "   " + str(num2) + "   " + str(num3) + "   "
        
        if num1 == num2 and num3 == num1:
            score += 50
            text = "You got three of a kind and +50 credits"
        elif num1 == num2 or num2 == num3 or num1 == num3:
            score += 20
            text = "You got two of a kind and +20 credits"
        else:
            text = "You lost"
            if score == 0:
                self.play["state"] = "disabled"
                self.add["state"] = "active"

        self.points.setNumber(score)
        self.points.config(justify="center")
        self.result.setText(text)
        self.result.config(justify="center")

    def addcred(self):
        self.points.setNumber("50")
        self.play["state"] = "active"
        self.add["state"] = "disabled"

    def cash(self):
        score = self.points.getNumber()
        total = self.points.getNumber()
        if score < 50:
            final = 50 - score
            text = "You lost " + str(final) + " credits in your last 50 credits leaving you with " + str(total) + " credits."
        elif score > 50:
            final = score - 50
            text = "Congratulations you won " + str(final) + " credits in your last 50 credits leaving you with " + str(total) + " credits!"
        else:
            text = "Congratulations you went even leaving you with " + str(total) + " credits!"
        self.messageBox(title="Cashout Window", message=text)
        SlotMachine.quit(self)


def main():
    SlotMachine().mainloop()


if __name__ == "__main__":
    main()
