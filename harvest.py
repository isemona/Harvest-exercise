############
# Part 1   #
############

# Game():
# def __init__(self, board, player1, player2, list index)

class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = False # Has seeds
        self.is_bestseller = False # Bestseller
        self.name = name
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    # musk 
    musk_melon = Melontype("musk",1998,"green",True,True)

    # self, code, first_harvest, color, is_seedless, is_bestseller, name
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    # casaba
    casaba = Melontype ("cas", 2003, "orange", True)
    casaba.add_pairing('strawberries', "mint")
    all_melon_types.append(casaba)

    # crenshaw
    crenshaw = Melontype('cren',1996,'green',True)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)


    #yellow watermelon
    yellow_watermelon = Melontype ('yw', 2013, 'yellow', True, True)
    yellow_watermelon.add_pairing ('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in all_melon_types:
        print("{} pairs with {}".format(melon))
        for pair in self.pairing:
            

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 






