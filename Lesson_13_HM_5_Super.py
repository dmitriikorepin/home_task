class SuperStr(str):
    def is_repeatance(self, s):
        if s == "":
            return False
        if self == "":
            return False
        if len(self) % len(s) != 0:
            return False

        count = len(self) // len(s)
        repeated = ""
        for _ in range(count):
            repeated += s
        return self == repeated

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()


test_a = SuperStr("abcabcabc")
print(test_a.is_repeatance("abc"))
print(test_a.is_repeatance("ab"))
print(test_a.is_repeatance(""))

test_b = SuperStr("Level")
print(test_b.is_palindrom())
