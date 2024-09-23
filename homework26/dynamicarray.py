from typing import Iterator, Any


class DynamicArray:
    def __init__(self, capacity: int=10, mutable: bool = True):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.mutable = mutable
        self.array = [None] * self.capacity #not sure about None

    def __getitem__(self, index: int):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def __setitem__(self, index: int, value: any) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def append(self, value: any) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1
        #print(self.size)

    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self) -> str:
        return str([self.array[i] for i in range(self.size)])

    def __repr__(self) -> str:
        return str(self.array)


    def __len__(self) -> int:
        return self.size

    def get_capacity(self) -> int:
        return self.capacity

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Operand must be of type DynamicArray")

        new_capacity = self.size + other.size
        new_array = DynamicArray(new_capacity)
        for i in range(self.size):
            new_array.append(self.array[i])

        for j in range(other.size):
            new_array.append(other.array[j])

        return new_array

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Operand must be of type DynamicArray")

        for i in range(other.size):
            self.append(other.array[i])

        return self

    def __eq__(self, other: 'DynamicArray') -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True


    def __ne__(self, other: 'DynamicArray') -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: 'DynamicArray') -> bool:
        if not isinstance(other, DynamicArray):
            raise TypeError("Can only compare with another DynamicArray")

        for i in range(min(len(self), len(other))):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        return len(self) < len(other)


    def __le__(self, other: 'DynamicArray') -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other: 'DynamicArray') -> bool:
        return not self.__le__(other)

    def __ge__(self, other: 'DynamicArray') -> bool:
        return not self.__lt__(other)

    def __iter__(self) -> Iterator[Any]:
        for i in range(self.size):
            yield self.array[i]

    def __hash__(self) :  #pure improvisation after a bit of research 
        if self.mutable:
            raise TypeError("DynamicArray is mutable; cannot compute hash.")
        hashed = (hash(self.array[i]) for i in range(self.size))
        return hashed


if __name__ == "__main__":

    array1 = DynamicArray()
    array2 = DynamicArray()

    array1.append(1)
    array1.append(2)
    array1.append(3)
    print(f"Array 1 after appending elements: {array1} ")

    array2.append(4)
    array2.append(5)
    print(f"Array 2 after appending elements: {array2} ")

    print(f"Element at index 1 in array1: {array1[1]}")

    array1[1] = 10
    print(f"Array 1 after modification: {array1}")

    for ele in range(4, 15):
        array1.append(ele)
    print(f"Array after appending elements: {array1}")

    combined_array = array1 + array2
    print(f"Combined Array: {combined_array}")

    array1 += array2
    print(f"Array 1 after in-place addition: {array1}")
