from inspect import classify_class_attrs


class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitems__(self, index, new_items):
        self.items[index] = new_items

    def __sum__(self):
        return [i+1 for i in range(1, 10)]
