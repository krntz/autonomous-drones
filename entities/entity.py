import numpy as np


class Entity:
    def __init__(self, uid: str, position: any = np.zeros(3)) -> None:
        self._position = position

        self._uid = uid

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def position(self) -> any:
        return self._position

    def update(self) -> None:
        raise NotImplementedError("All entities need an update function!")
