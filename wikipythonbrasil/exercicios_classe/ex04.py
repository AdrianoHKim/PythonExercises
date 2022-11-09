""" 4.Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhecer, engordar, emagrecer, crescer.
Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos,ela deve crescer 0,5 cm."""


class Person:
    def __init__(self, name: str, age: int, weight: int, height: float):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def getolder(self):
        print('Person age: {} years.'.format(self.age))
        question1 = input('Do you wish to age the person? [y/n]: ').lower()
        if question1 == 'y':
            age2 = int(input('Type the age: '))
            if self.age + age2 < 21:
                self.height = ((age2 * 0.5) + float(self.height))
                self.age = self.age + age2
            if self.age + age2 > 21:
                self.height = (((21 - self.age) * 0.5) + float(self.height))
                self.age = self.age + age2
            else:
                self.age = self.age + age2

    def gainweight(self):
        print('Person weight: {} kgs.'.format(self.weight))
        question2 = input('Do you wish the person to gain weight? [y/n]: ').lower()
        if question2 == 'y':
            weight2 = int(input('Type the weight (kg): '))
            self.weight = self.weight + weight2

    def loseweight(self):
        print('Person weight: {} kgs.'.format(self.weight))
        question3 = input('Do you wish the person to lose weight? [y/n]: ').lower()
        if question3 == 'y':
            weight2 = int(input('Type the weight (kg): '))
            self.weight = self.weight - weight2

    def gainheight(self):
        print('Person height: {} cm.'.format(self.height))
        question4 = input('Do you wish the person to gain height? [y/n]: ').lower()
        if question4 == 'y':
            height2 = int(input('Type the height (cm): '))
            self.height = self.height + height2

    def infos(self):
        print('\nPerson information:\nName: {}\nAge: {} years\nWeight: {} kgs.'
              '\nHeight: {} cm.'.format(self.name, self.age, self.weight, self.height))


def main():
    person1 = Person('Adriano', 15, 62, 180)  # edit info here (name, age, weight, height)

    while True:
        person1.gainweight()
        person1.loseweight()
        person1.gainheight()
        person1.getolder()
        person1.infos()
        loopy = input('\nDo you wish to make another operation? [y/n]: ').lower()
        if loopy == "n":
            print('Program finished.')
            break


if __name__ == '__main__':
    main()
