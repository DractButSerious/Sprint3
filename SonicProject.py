from enum import Enum
import unittest

# Create Size enums.
class Size(Enum):
    """
    An enumeration of different size categories.

    Attributes:
        NULL: No size set.
        SMALL: Represents the smallest size.
        MEDIUM: Represents the medium size.
        LARGE: Represents the large size.
        MEGA: Represents the largest size.
    """
    def __str__(self):
        return str(self.value)
    NULL = None
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    MEGA = "Mega"

class Foods(Enum):
    """
    An enumeration of different food categories.

    Attributes:
        NULL: Default; none set
        HOT_DOG: Hot Dog ($2.30)
        CORN_DOG: Corn Dog ($2.00)
        ICE_CREAM: Ice Cream ($3.00)
        ONION_RINGS: Onion Rings ($1.75)
        FRIES: French Fries ($1.50)
        TOTS: Tater Tots ($1.70)
        NACHOS: Nacho Chips ($1.90)
    """
    def __str__(self):
        return str(self.value)
    NULL = None
    HOT_DOG = "Hot Dog"
    CORN_DOG = "Corn Dog"
    ICE_CREAM = "Ice Cream"
    ONION_RINGS = "Onion Rings"
    FRIES = "French Fries"
    TOTS = "Tater Tots"
    NACHOS = "Nacho Chips"

class Topping(Enum):
    """
    An enumeration of different topping categories.

    Attributes:
        CHERRY: Cherry (Free)
        WHIPPED_CREAM: Whipped Cream (Free)
        KETCHUP: Ketchup (Free)
        MUSTARD: Mustard (Free)
        CHEESE: Nacho Cheese ($0.30)
        BACON: Bacon Bits ($0.30)
        CARAMEL: Caramel Sauce ($0.50)
        CHOCOLATE: Chocolate Sauce ($0.50)
        CHILI: Chili ($0.60)
    """
    def __str__(self):
        return str(self.value)
    CHERRY = "Cherry"
    WHIPPED_CREAM = "Whipped Cream"
    KETCHUP = "Ketchup"
    MUSTARD = "Mustard"
    CHEESE = "Nacho Cheese"
    BACON = "Bacon Bits"
    CARAMEL = "Caramel Sauce"
    CHOCOLATE = "Chocolate Sauce"
    CHILI = "Chili"

# Create class "Drink"
class Drink:
    """
    A class for storing a drink object.

    Attributes:
        _base (str): The base of the drink (e.g., "Water", "Sprite").
        _flavors (set): A set of flavors in the drink (e.g., {"Lemon", "Cherry"}).
    """
    
    # Initialize the valid bases and flavors.
    _valid_bases = {"water", "sprite", "coca-cola", "dr. pepper", "starry", "root beer"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    _valid_sizes = {Size.SMALL, Size.MEDIUM, Size.LARGE, Size.MEGA}

    # Initialize with no base and an empty flavor list.
    def __init__(self, size):
        """
        Initializes an empty `Drink` object.

        Args:
            size (str): The new size for the drink. Valid sizes are "Small", "Medium", "Large", and "Mega", or the `Size` enums for them.

        Raises:
            ValueError: If the size is invalid.
        """
        self._base = None
        self._flavors = set()
        self._size = size
        self._cost = 0.00

    # Return the _base property.
    def get_base(self):
        """
        Returns the base of the drink.

        Returns:
            str: The base of the drink.
        """
        return self._base
    
    # Return the _flavors property.
    def get_flavors(self):
        """
        Returns the flavors of the drink as a list.

        Returns:
            list: A list of the drink's flavors.
        """
        return list(self._flavors)
    
    # Return the number of flavors.
    def get_num_flavors(self):
        """
        Returns the number of flavors in the drink.

        Returns:
            int: The number of flavors.
        """
        return len(self._flavors)

    def get_size(self):
        """
        Returns the size of the drink.

        Returns:
            str: Drink size.
        """
        return self._size
    
    # Set the drink's _base property.
    def set_base(self, base):
        """
        Sets the base of the drink.

        Args:
            base (str): The new base for the drink. Valid bases are "Water", "Sprite", "Coca-Cola", "Dr. Pepper", "Starry", and "Root Beer".

        Raises:
            ValueError: If the base is invalid.
        """
        if base.casefold() in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")
    
    # Add a flavor to the _flavors property.
    def add_flavor(self, flavor):
        """
        Adds a flavor to the drink.

        Args:
            flavor (str): The flavor to add. Valid flavors are "Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", and "Lime".

        Raises:
            ValueError: If the flavor is invalid.
        """
        if flavor.casefold() in self._valid_flavors:
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")

    # Set the _flavors property to a given list.
    def set_flavors(self, flavors):
        """
        Sets the flavors of the drink.

        Args:
            flavors (list): A list of flavors to set. Valid flavors are "Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", and "Lime".

        Raises:
            ValueError: If any of the flavors are invalid.
        """
        for flavor in flavors:
            if flavor.casefold() not in self._valid_flavors:
                raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)
    
    def set_size(self, size):
        """
        Sets the size of the drink.

        Args:
            size (str): The new size for the drink. Valid sizes are "Small", "Medium", "Large", and "Mega", or the `Size` enums for them.

        Raises:
            ValueError: If the size is invalid.
        """
        if size.casefold() in self._valid_sizes:
            self._size = size
        else:
            raise ValueError(f"Pick a proper size from {self._valid_sizes}.")
    
    def calculate_cost(self):
        """
        Calculates and returns the cost of the drink.

        Returns:
            float: The cost of the drink.
        """
        base_cost = 0.00
        match self._size:
            case Size.SMALL:
                base_cost = 1.50
            case Size.MEDIUM:
                base_cost = 1.75
            case Size.LARGE:
                base_cost = 2.05
            case Size.MEGA:
                base_cost = 2.15
        return base_cost + len(self._flavors) * 0.15


# Create class "Food"
class Food:
    """
    A class for storing a Food object.

    Attributes:
        _base (str): The base of the drink (e.g., "Hot Dog", "Onion Rings"). Foods enums can also be used.
        _toppings (set): A set of flavors in the drink (e.g., {"Lemon", "Cherry"}).
    """

    _valid_bases = {"hot dog", "corn dog", "ice cream", "onion rings", "french fries", "tater tots", "nacho chips"}
    _valid_toppings = {"cherry", "whipped cream", "caramel sauce", "chocolate sauce", "nacho cheese", "chili", "bacon bits", "ketchup", "mustard"}

    def __init__(self):
        """
        Initializes an empty `Food` object.
        """
        self._base = Foods.NULL
        self._toppings = set()
        self._cost = 0.00
    
    # Return the _base property.
    def get_base(self):
        """
        Returns the base of the food.

        Returns:
            str: The base of the food.
        """
        return self._base
    
    # Return the _toppings property.
    def get_toppings(self):
        """
        Returns the toppings of the food as a list.

        Returns:
            list: A list of the drink's toppings.
        """
        return list(self._toppings)
    
    # Return the number of toppings.
    def get_num_toppings(self):
        """
        Returns the number of flavors in the food.

        Returns:
            int: The number of toppings.
        """
        return len(self._toppings)

    # Set the food's _base property.
    def set_base(self, base):
        """
        Sets the base of the food.

        Args:
            base (str): The new base for the food. Valid bases are any Foods enum value aside from Foods.NULL.

        Raises:
            ValueError: If the base is invalid.
        """
        if base.value.casefold() in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")
    
    # Add a topping to the _toppings property.
    def add_topping(self, topping):
        """
        Adds a topping to the drink.

        Args:
            topping (str): The topping to add. Valid topping are any Toppings enum.

        Raises:
            ValueError: If the topping is invalid.
        """
        if topping.value.casefold() in self._valid_toppings:
            self._toppings.add(topping)
        else:
            raise ValueError(f"Pick a proper topping from {self._valid_toppings}.")

    # Set the _toppings property to a given list.
    def set_toppings(self, toppings):
        """
        Sets the toppings on the food.

        Args:
            toppings (list): A list of toppings to set. Valid toppings are all Topping enums (e.g. Topping.CHERRY)

        Raises:
            ValueError: If any of the toppings are invalid.
        """
        for topping in toppings:
            if topping.value.casefold() not in self._valid_toppings:
                raise ValueError(f"Pick a proper topping from {self._valid_toppings}.")
        self._toppings = set(toppings)
    
    def calculate_cost(self):
        """
        Calculates and returns the cost of the food.

        Returns:
            float: The cost of the food.
        """
        base_cost = 0.00
        topping_cost = 0.00
        match self._base:
            case Foods.HOT_DOG: base_cost = 2.30
            case Foods.CORN_DOG: base_cost = 2.00
            case Foods.ICE_CREAM: base_cost = 3.00
            case Foods.ONION_RINGS: base_cost = 1.75
            case Foods.FRIES: base_cost = 1.50
            case Foods.TOTS: base_cost = 1.70
            case Foods.NACHOS: base_cost = 1.90
        for topping in list(self._toppings):
            match topping:
                case Topping.CHERRY | Topping.WHIPPED_CREAM | Topping.KETCHUP | Topping.MUSTARD:
                    continue
                case Topping.CHEESE | Topping.BACON:
                    topping_cost += 0.30
                case Topping.CARAMEL | Topping.CHOCOLATE:
                    topping_cost += 0.50
                case Topping.CHILI:
                    topping_cost += 0.60
        return base_cost + topping_cost

# Create class "Order"
class Order:
    """
    A class representing an order of drinks.

    Attributes:
        _items (list): A list of `Drink` objects in the order.
    """
    # Give the class instance its _items property.
    def __init__(self):
        """Initializes an empty order."""
        self._items = []
    
    # Return the list of items in this instance.
    def get_items(self):
        """
        Returns a list of `Drink` objects in the order.

        Returns:
            list: A list of `Drink` objects.
        """
        return self._items

    # Return the number of items in this instance.
    def get_total(self):
        """
        Returns the total number of items in the order.

        Returns:
            int: The number of items in the order.
        """
        return len(self._items)
    
    # List out every item in the list.
    def get_receipt(self):
        """
        Generates a formatted receipt for the order.

        Returns:
            str: A formatted string representing the receipt.
        """
        receipt = "Your order receipt:\n"
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            # Formats the "flavors" string like "Lemon, Mint, Blueberry"
            flavors = ", ".join(drink.get_flavors())

            price = drink.calculate_cost()
            # Example: "1: Base - Root Beer, Flavors - Lemon, Cherry"
            receipt += f"{i + 1}: Base - {base}, Flavors - {flavors}, Price - ${price}\n"
        return receipt
    
    # Add a Drink instance to the end of the list.
    def add_item(self, drink):
        """
        Adds a `Drink` object to the order.

        Args:
            drink (Drink): The `Drink` object to add.

        Raises:
            ValueError: If the argument is not a `Drink` object.
        """
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            # If the instance is not a Drink, throw an error.
            raise ValueError("You can only add drinks to this order.")
    
    # Remove a Drink instance from the list based on index.
    def remove_item(self, index):
        """
        Removes a `Drink` object from the order at the specified index.

        Args:
            index (int): The index of the item to remove.

        Raises:
            IndexError: If the index is invalid.
        """
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            # If the index is outside of the list, i.e. invalid, throw an error.
            raise IndexError("Invalid index, cannot remove item.")

class MethodTests(unittest.TestCase):

    def test_drink(self):
        item = Drink(Size.SMALL)
        item.set_base("Sprite")
        item.set_flavors({"Lemon", "Cherry"})
        item.add_flavor("Lime")
        self.assertEqual(item.calculate_cost(), 1.50 + 0.15 * 3)

    def test_food(self):
        item = Food()
        item.set_base(Foods.HOT_DOG)
        item.set_toppings({Topping.BACON, Topping.CHEESE})
        item.add_topping(Topping.CHILI)
        item.add_topping(Topping.KETCHUP)
        self.assertEqual(item.calculate_cost(), 3.50, "This food item should be $3.50.")

test = MethodTests()
test.test_food()
