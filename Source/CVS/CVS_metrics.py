import enum


class GateTransCost(enum.Enum):
    # num of transistors per gate
    AND = 6
    OR = 6
    NOT = 2
    NAND = 4
    NOR = 4
    XOR = 8


class GateDelay(enum.Enum):
    # num of transistors per gate
    AND = 0
    OR = 0
    NOT = 0
    NAND = 0
    NOR = 0
    XOR = 0
