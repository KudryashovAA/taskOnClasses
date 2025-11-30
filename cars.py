"""Task on classes and inheritance"""

from csv import reader
from os.path import splitext
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List


class BaseCar:
    """Base class for cars and special machinery"""

    def __init__(
            self,
            brand: "str",
            photo_file_name: "str",
            carrying: "float",
            car_type: "str"
    ):
        """Base class constructor"""

        self.brand: "str" = brand
        self.photo_file_name: "str" = photo_file_name
        self.carrying: "float" = carrying
        self.car_type: "str" = car_type

    def __repr__(self) -> "str":
        """String representation of an object"""

        return f"{self.car_type}: {self.brand} {self.carrying}"

    def get_photo_file_ext(self) -> "str":
        """Provides the photo file extension"""

        return splitext(self.photo_file_name)[1]


class Car(BaseCar):
    """Passenger car class"""

    def __init__(
            self,
            brand: "str",
            photo_file_name: "str",
            carrying: "float",
            passenger_seats_count: "int",
    ):
        """Constructor of the passenger car class"""

        super().__init__(brand, photo_file_name, carrying, "car")
        self.passenger_seats_count: "int" = passenger_seats_count

    def __repr__(self) -> "str":
        """String representation of an object"""

        return f"{self.car_type}: {self.brand} {self.carrying} {self.passenger_seats_count}"


class Truck(BaseCar):
    """Constructor of the truck class"""

    def __init__(
            self,
            brand: "str",
            photo_file_name: "str",
            carrying: "float",
            body_whl: "str",
    ):
        """Constructor of the truck class"""

        super().__init__(brand, photo_file_name, carrying, "truck")

        self.body_width: "float" = 0.0
        self.body_height: "float" = 0.0
        self.body_length: "float" = 0.0

        if body_whl and body_whl.strip():
            try:
                parts = body_whl.split("x", maxsplit=2)
                if len(parts) == 3:
                    self.body_width, self.body_height, self.body_length = map(float, parts)
                else:
                    raise ValueError("Expected exactly 3 dimensions separated by 'x'")
            except ValueError as error:
                raise ValueError(f"Invalid body_whl format: {body_whl}") from error

    def get_body_volume(self) -> "float":
        """Returns the body volume in cubic meters"""

        return self.body_width * self.body_height * self.body_length

    def __repr__(self) -> "str":
        """String representation of an object"""

        return f"{self.car_type}: {self.brand} {self.carrying} {self.body_width}x{self.body_height}x{self.body_length}"


class SpecMachine(BaseCar):
    """Special machinery class"""

    def __init__(
            self,
            brand: "str",
            photo_file_name: "str",
            carrying: "float",
            extra: "str",
    ):
        """Constructor of the special machinery class"""

        super().__init__(brand, photo_file_name, carrying, "spec_machine")
        self.extra: "str" = extra

    def __repr__(self) -> "str":
        """String representation of an object"""

        return f"{self.car_type}: {self.brand} {self.carrying} {self.extra}"


def get_car_list(csv_filename: "str") -> "List[BaseCar]":
    """Reading data from a CSV file and representing it as a list of objects"""

    car_list: "List[BaseCar]" = []

    with open(csv_filename, encoding="UTF-8") as csv_fd:
        for i, row in enumerate(reader(csv_fd, delimiter=";")):
            if i and len(row) == 7:
                try:
                    if row[0] == "car":
                        car_list.append(
                            Car(row[1], row[3], float(row[5]), int(row[2]))
                        )

                    elif row[0] == "truck":
                        car_list.append(
                            Truck(row[1], row[3], float(row[5]), row[4])
                        )

                    elif row[0] == "spec_machine":
                        car_list.append(
                            SpecMachine(row[1], row[3], float(row[5]), row[6])
                        )
                except ValueError:
                    continue

    return car_list


if __name__ == "__main__":
    list_cars = get_car_list("cars.csv")

    for line in list_cars:
        print(line)
