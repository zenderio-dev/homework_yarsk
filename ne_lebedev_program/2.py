class User:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.isalpha() or not new_name:
            raise ValueError("Некорректное имя")
        self.__name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError("Некорректный возраст")
        self._age = new_age

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age


if __name__ == "__main__":
    try:
        user1 = User("Alice", 30)
        print("Имя пользователя:", user1.get_name())
        print("Возраст пользователя:", user1.get_age())

        user1.set_name("Bob")
        user1.set_age(35)

        print("Имя пользователя после изменения:", user1.get_name())
        print("Возраст пользователя после изменения:", user1.get_age())

        user1.set_name("")
    except ValueError as e:
        print("Исключение:", e)

    try:
        user1.set_age(-5)
    except ValueError as e:
        print("Исключение:", e)

    try:
        user2 = User("John123", 25)
    except ValueError as e:
        print("Исключение:", e)

    try:
        user3 = User("Alice", 150)
    except ValueError as e:
        print("Исключение:", e)
