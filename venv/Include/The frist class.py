"""
根据python crash course 仿照第一个例子敲的实例
"""
class Dog():
    """Dog类"""

    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled overd!")

my_dog = Dog('caixueqi',20)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's is " + str(my_dog.age)  +  " yea    rs old.")
my_dog.sit()
my_dog.roll_over()