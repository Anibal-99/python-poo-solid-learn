from dataclasses import dataclass

@dataclass
class ThreeDPoint:
    x: int | float
    y: int | float
    z: int | float

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hello {name}! This is your 3D point!")


point_1 = ThreeDPoint(1, 2, 3)
print(point_1)
point_2 = ThreeDPoint(1.0, 2.0, 4.0)
print(point_2)

print(point_1==point_2)
