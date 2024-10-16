# region ZAD 1
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = int(mileage)


red = Car("red", 20000)
blue = Car("blue", 30000)

print(f"The {blue.color} car has {blue.mileage} miles.")
print(f"The {red.color} car has {red.mileage} miles.")


# endregion

# region ZAD 2
class MyWater:
    def __init__(self):
        self.small = 0
        self.medium = 0
        self.large = 0

        self.capacity = 0

    def add_large(self, amount):
        for i in range(amount):
            self.large += 1
            self.capacity += 2

    def add_medium(self, amount):
        for i in range(amount):
            self.medium += 1
            self.capacity += 1

    def add_small(self, amount):
        for i in range(amount):
            self.small += 1
            self.capacity += 0.5

    def get_capacity(self):
        return self.capacity

    def get_large(self):
        return self.large

    def get_medium(self):
        return self.medium

    def get_small(self):
        return self.small


water = MyWater()
water.add_large(2)
water.add_medium(1)
water.add_small(3)

print("")

print(f"Mam teraz {water.get_capacity()} litrów wody")
print(f"Dużych butelek : {water.get_large()}")
print(f"Średnich butelek : {water.get_medium()}")
print(f"Małych butelek : {water.get_small()}")

# endregion

# region ZAD 3
print("")


class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def join_diagonal(self, other_box):
        return Box(self.width + other_box.width, self.height + other_box.height)

    def join_horizontal(self, other_box):
        width = self.width + other_box.width
        height = self.height
        if height < other_box.height:
            height = other_box.height
        return Box(width, height)
        pass

    def join_vertical(self, other_box):
        width = self.width
        height = self.height + other_box.height
        if width < other_box.width:
            width = other_box.width
        return Box(width, height)
        pass

    def __str__(self):
        pass


def test_box_operations():
    # Tworzymy dwa pudełka o znanych szerokościach
    box1 = Box(5, 10)
    box2 = Box(3, 6)

    # Test połączenia diagonalnego
    diagonal_box = box1.join_diagonal(box2)

    if diagonal_box.width == 8 and diagonal_box.height == 16:
        print("Test połączenia diagonalnego: SUKCES")
    else:
        print(f"Test połączenia diagonalnego: PORAŻKA (Oczekiwano: szerokość 8, wysokość 16, "
              f"Otrzymano: szerokość {diagonal_box.width}, wysokość {diagonal_box.height})")

    # Test połączenia poziomego
    horizontal_box = box1.join_horizontal(box2)
    if horizontal_box.width == 8 and horizontal_box.height == 10:
        print("Test połączenia poziomego: SUKCES")
    else:
        print(f"Test połączenia poziomego: PORAŻKA (Oczekiwano: szerokość 8, wysokość 10, "
              f"Otrzymano: szerokość {horizontal_box.width}, wysokość {horizontal_box.height})")

    # Test połączenia pionowego
    vertical_box = box1.join_vertical(box2)
    if vertical_box.width == 5 and vertical_box.height == 16:
        print("Test połączenia pionowego: SUKCES")
    else:
        print(f"Test połączenia pionowego: PORAŻKA (Oczekiwano: szerokość 5, wysokość 16, "
              f"Otrzymano: szerokość {vertical_box.width}, wysokość {vertical_box.height})")
    print()
    print("Wszystko działa, brawo")


test_box_operations()

# endregion

# region ZAD 4

print("")


class Pesel:
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def __init__(self, pesel):
        self.pesel = pesel

    def is_valid(self):
        control_sum = 0
        for index, j in enumerate(self.pesel):
            if (index == 10):
                break
            digit = int(j)
            control_sum += digit * self.weights[index]

        modulo = control_sum % 10
        if modulo == 0:
            if modulo != int(self.pesel[10]):
                return False

            return True

        sum_control = 10 - modulo
        if (sum_control != int(self.pesel[10])):
            return False
        return True

    def check_sex(self):
        if int(self.pesel[9]) % 2 == 0:
            return "K"
        else:
            return "M"

    def show_data(self):
        print(f"Płeć: {self.check_sex()}")
        if (pesel.is_valid()):
            print("Pesel jest poprawny")
        else:
            print("Pesel jest niepoprawny")


# pesel = Pesel(input("Podaj pesel: "))

pesel = Pesel("55030101193")

pesel.show_data()


# endregion

# region ZAD 5

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produkt: {self.name}, cena: {self.price}"


class DiscountCalculator:
    over_x_discount_amount = 300
    over_x_discount = 0.05
    free_glass_discount_amount = 200

    def __init__(self):
        self.products = []

    def discount_by_percatange(self):
        total_price = self.get_total_price()

        if total_price > self.over_x_discount_amount:
            return total_price - (total_price * self.over_x_discount)

        return total_price

    def three_for_two(self):
        if len(self.products) < 3:
            return self.products

        self.products.sort(key=lambda x: x.price, reverse=True)
        self.products[2].price = 0
        return self.products

    def add_free_glass(self):
        czySzklanka = False
        for product in self.products:
            if product.name == "Szklanka":
                czySzklanka = True
                break
        if not czySzklanka:
            if  self.get_total_price() > self.free_glass_discount_amount:
                self.products.append(Product("Szklanka", 0))
                return True

    def calculate_discounts(self):
        self.three_for_two()
        self.add_free_glass()

        return self.products

    def get_total_price(self):
        total_price = 0
        for product in self.products:
            total_price += product.price
        return total_price


class ProductsSorter:

    @staticmethod
    def sort(products):
        products.sort(key=lambda x: x.price)
        return products

    @staticmethod
    def most_expensive(products):
        for product in products:
            if product.price == max(products, key=lambda x: x.price).price:
                return product

    @staticmethod
    def the_cheapest(products):
        min = products[0]
        for product in products:
            if product.price < min.price:
                min = product
        return min

    @staticmethod
    def the_cheapest_n(products, n):
        products.sort(key=lambda x: x.price)
        return products[:n]


class Basket:
    discountCalculator = DiscountCalculator()
    productsSorter = ProductsSorter()

    def __init__(self):
        self.products = []

    def add_item(self, product):
        self.discountCalculator.products.append(product)

        self.discountCalculator.add_free_glass()

        self.products.append(product)

    def show_products(self):
        self.products = self.productsSorter.sort(self.products)
        for product in self.products:
            print(product)

    def get_cheapest_n(self, n):
        return self.productsSorter.the_cheapest_n(self.products, n)

    def get_cheapest(self):
        return self.productsSorter.the_cheapest(self.products)

    def get_most_expensive(self):
        return self.productsSorter.most_expensive(self.products)
    def show_price(self):
        self.products = self.discountCalculator.calculate_discounts()

        total_price = self.discountCalculator.discount_by_percatange()

        for product in self.products:
            print(product)
        print(f"Cena: {total_price}")


basket = Basket()
basket.add_item(Product("Chleb", 200))
basket.add_item(Product("Masło", 500))
basket.add_item(Product("Mleko", 300))

print("")

print("Produkty:")
basket.show_products()

print("\nNajtanszy produkt:")
print(basket.get_cheapest())

print("\nNajdroższy produkt:")
print(basket.get_most_expensive())

print("\nNajtansze 2 produkty:")
for i in basket.get_cheapest_n(2):
    print(i)

print("\nCena za produkty")
basket.show_price()
# endregion
