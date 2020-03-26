class Animal:
    def __init__(self, name, species, no_legs, noise):
        self.name = name
        self.no_legs = no_legs
        self.noise = noise
        self.species = species

    def talk(self):
        '''Returns the name of the animal and the sound it makes'''
        print(f'{self.name} yields {self.noise}')


class Bird(Animal):
    def __init__(self, name, species, noise):
        super().__init__(name, species, 2, noise)
        self.has_feathers = True

    def __str__(self):
        '''Returns the name and the description(species and number of legs) of the bird'''
        return f'{self.name} of species {self.species} is a bird and has {self.no_legs} legs'


class Mammal(Animal):
    def __init__(self, name, species, noise):
        super().__init__(name, species, 4, noise)
        self.has_fur = True

    def __str__(self):
        '''Returns the name and the description(species and number of legs) of the mammal'''
        return f'{self.name} of species {self.species} is a mammal and has {self.no_legs} legs'


class Utils:
    '''Utilities class'''

    MAX_NO_FAULTS = 3

    @staticmethod
    def print_menu():
        '''Prints all the menu items for the user to choose'''
        Utils.print_spacing()
        print('(i)nsert animal')
        print('(d)elete animal')
        print('(l)ist animals')
        print('(m)ake noise!')
        print('(c)ount')
        print('e(x)it')

    @staticmethod
    def print_spacing():
        '''Prints a number of * characters as a delimiter between user interactions'''
        print('*' * 13)

    @staticmethod
    def is_user_input_correct(name, species, sound):
        '''Verifies if the provided user input is valid'''
        return name and species and sound


class Zoo:
    '''
    Contains a list of all the animals in the zoo
        and provides the necessary operations for managing the zoo.
    '''

    def __init__(self):
        '''Initialize the container for all the animals'''
        self.all_animals = []

    def list_all_animals(self):
        '''Print all the animals currently present int he zoo'''
        if self.all_animals:
            for animal in self.all_animals:
                print(animal)
        else:
            print('No animals in the zoo at this moment!')

    def all_animals_talk(self):
        '''Make all the animals talk by invoking the function with the same name'''
        if self.all_animals:
            for animal in self.all_animals:
                animal.talk()
        else:
            print(':( there\'s nobody around to make the noise! :(')

    def add_new_animal(self, animal):
        '''Add a new animal in the container'''
        self.all_animals.append(animal)

    def remove_animal(self, name):
        '''Remove an animal from the container'''
        for animal in self.all_animals:
            if animal.name.upper() == name.upper():
                self.all_animals.remove(animal)

    def count_heads_and_legs(self):
        '''Creates a statistic about the number of heads and legs within the zoo'''
        leg_count = 0
        head_count = 0

        for animal in self.all_animals:
            head_count += 1
            leg_count += animal.no_legs

        return f'The zoo has a head count of {head_count} with {leg_count} legs'


#############
# counter for the invalid number of worn menu choices
faults = 0

# create the zoo and populate it with animals
zoo = Zoo()
zoo.add_new_animal(Mammal('oli', 'tiger', 'roar'))
zoo.add_new_animal(Bird('tuk', 'tucan', 'tuktuk'))

# show the menu and execute menu actions until the user exits
while True:
    Utils.print_menu()
    user_input = input('Make a choice from the menu:')
    Utils.print_spacing()

    if user_input.upper() == 'X':
        print('Bye!')
        break
    elif user_input.upper() == 'L':
        # listing all the animals
        zoo.list_all_animals()
    elif user_input.upper() == 'C':
        # print the heads & legs count
        print(zoo.count_heads_and_legs())
    elif user_input.upper() == 'M':
        # make all animals talk
        zoo.all_animals_talk()
    elif user_input.upper() == 'D':
        # remove an animal
        animal_name_input = input('Name of the animal you want to remove:')
        zoo.remove_animal(animal_name_input)
    elif user_input.upper() == 'I':
        # add a new animal
        animal_type_in = input('Specify the type of animal (bird or mammal):')
        animal_name_in = input('Specify the name of the animal:')
        animal_species_in = input('Specify the species of the animal:')
        animal_sound_in = input('Specify the sound the animal makes:')

        if Utils.is_user_input_correct(animal_name_in, animal_species_in, animal_sound_in):
            if animal_type_in.upper() == 'BIRD':
                zoo.add_new_animal(Bird(animal_name_in, animal_species_in, animal_sound_in))
                print('New bird successfully added!')
            elif animal_type_in.upper() == 'MAMMAL':
                zoo.add_new_animal(Mammal(animal_name_in, animal_species_in, animal_sound_in))
                print('New mammal successfully added!')
            else:
                print('Unrecognized animal category!')
    else:
        # handle invalid inputs from user
        if faults >= Utils.MAX_NO_FAULTS:
            print('You\'re too stupid for this! Exiting.')
            break
        print('Unrecognized command, please try again!')
        faults += 1
