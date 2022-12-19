from pydantic import BaseModel


class BaseGroup(BaseModel):
    """Базовый класс для описания группы"""

    name :str

class GroupIn(BaseGroup):
    """Класс описывает  группу, полученную от пользователя"""

    pass

class GroupOut(BaseGroup):
    """Класс описывает группу, отправленную пользователю"""

    id :int

class GroupStorage(BaseGroup):
    """Класс описывает хранимую группу в хранилище"""

    id :int