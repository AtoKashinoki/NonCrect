

from NonCrect.ComponentSkeleton import ComponentSkeleton
from NonCrect.DataClass import Components
from NonCrect.Definition import ComponentType


class Test(ComponentSkeleton):

    def __init__(self):
        super().__init__(ComponentType.NoneType)
        return

    def __process__(self, _object):
        return


if __name__ == '__main__':
    components = Components(Test)
    components.add_value_type(Test)
    components.append(Test())
    for component in components.values():
        print(component)
    ...
