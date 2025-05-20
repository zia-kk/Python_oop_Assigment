# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count=0

    def __init__(self):
        Counter.count +=1

    @classmethod #is ka matlab hai agla function class per kaam kray ga
    def counting_class(cls):
        print(f"Tota object is:{cls.count} " )
if __name__ == "__main__":

    obj1=Counter()
    obj2=Counter()

    Counter.counting_class()


