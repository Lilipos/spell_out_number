class Hiker:

    def __init__(self, val):
        self.num = str(val)

    def out(self):
        unit = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine"
            }
        tens = {
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
            }
        dec = {
            "2": "twenty",
            "3": "thirty",
            "4": "forty",
            "5": "fifty",
            "6": "sixty",
            "7": "seventy",
            "8": "eighty",
            "9": "ninety"
            }
        word = ""
        pom = len(self.num)
        div = pom // 3
        if pom % 3 == 0:
            div = div - 1
        dl = pom - div * 3
        i = 0
        while pom > 0:
            if dl == 0:
                dl = 3
                if div == 1:
                    word = word + " thousand, "
                    div = div - 1
                if div == 2:
                    word = word + " million, "
                    div = div - 1
            if self.num[i] == "0":
                dl = dl - 1
                i = i + 1
                pom = pom - 1
                continue
            if dl == 3:
                word = word + unit[self.num[i]] + " hundred"
            if dl == 2 and self.num[i] == "1":
                if i == 0:
                    word = tens[self.num[i] + self.num[i + 1]]
                else:
                    word = word + " and " + tens[self.num[i] + self.num[i + 1]]
                dl = dl - 2
                pom = pom - 2
                i = i + 2
                continue
            if dl == 2 and self.num[i] != "1":
                if i == 0:
                    word = dec[self.num[i]]
                elif self.num[i - 1] != "0":
                    word = word + " " + dec[self.num[i]]
                else:
                    word = word + " and " + dec[self.num[i]]
            if dl == 1:
                if i == 0:
                    word = dec[self.num[i]]
                elif self.num[i - 1] != "0":
                    word = word + " " + unit[self.num[i]]
                else:
                    word = word + " and " + unit[self.num[i]]
            dl = dl - 1
            i = i + 1
            pom = pom - 1
        return word
