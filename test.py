import collections
import threading

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

print([ j+i for i in range(2) for j in range(2)])

class A():
    def __init__(self):
        pass
    def __len__(self):
        return 100
    def __repr__(self):
        return "yo"
    @classmethod
    def a(cls):
        print(1)
    @staticmethod
    def b():
        print(2)
print(len(A()))
A.a()
A.b()
# print(A().a())


class a():
    def __new__(cls, *args, **kwargs):
        print(555)
class S():
    def __init__(self):
        pass
    # @classmethod
    # def __new__(cls, *args, **kwargs):
    #     print(">>>>>")
    #     # print()
    #     # print(args)


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            print("not")
            # print(Singleton._instance_lock)
            with Singleton._instance_lock:
                print("....")
                if not hasattr(cls, '_instance'):
                    print("123>>>>")
                    Singleton._instance = super().__new__(cls)
                else:
                    print(111111)
            return Singleton._instance
        else:
            print("-----")
ccc = Singleton(1)
ccc1 = Singleton(1)