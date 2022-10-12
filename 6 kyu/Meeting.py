# I don't care that tuples work like that
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __lt__(self, other):
        return (self.surname, self.name) < (other.surname, other.name)

    def __gt__(self, other):
        return (self.surname, self.name) > (other.surname, other.name)

    def __le__(self, other):
        return (self.surname, self.name) <= (other.surname, other.name)

    def __ge__(self, other):
        return (self.surname, self.name) >= (other.surname, other.name)

    def __eq__(self, other):
        return (self.surname, self.name) == (other.surname, other.name)

    def __repr__(self):
        return f"({self.surname.upper()}, {self.name.upper()})"

    def __str__(self):
        return self.__repr__()


def meeting(names):
    arr = [Person(*i.split(":")) for i in names.lower().split(";")]
    return "".join([str(i) for i in sorted(arr)])
