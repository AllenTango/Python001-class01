# 定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    Animal_Type = {"食肉": 1, "食草": 2, "杂食": 3}
    Animal_Size = {"小": 1, "中等": 2, "巨": 3}
    Animal_Character = {"凶猛": 1, "温顺": 2, "冷漠": 3}
    
    @abstractmethod
    def __init__(self, animal_type, animal_size, animal_character):
        self.animal_type = animal_type
        self.animal_size = animal_size
        self.animal_character = animal_character

    @property
    def is_ferocious(self):
        return self.Animal_Type[self.animal_type] == 1 and self.Animal_Size[self.animal_size] >= 2 and self.Animal_Character[self.animal_character] == 1


class Cat(Animal):
    meo = "🐱喵～"

    def __init__(self, name, cat_type, cat_size, cat_character):
        super().__init__(cat_type, cat_size, cat_character)
        self.name = name

    @property
    def is_pet(self):
        return not self.is_ferocious


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
        self.__dict__[animal.__class__.__name__] = self.animals


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    # a = Animal('食肉', '小', '温顺') # TypeError
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫 2', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
    print(cat2.is_pet)
