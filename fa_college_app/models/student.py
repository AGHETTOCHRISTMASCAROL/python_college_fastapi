import uuid
import datetime
from pydantic import BaseModel

class BaseStudent(BaseModel):
    """Базовый класс для описания студента"""

    first_name :str
    last_name :str
    age :int
    birth_date :datetime.date

class StudentIn(BaseStudent):
    """Класс описывает студента, полученного от пользователя"""
    
    login :str
    password :str

class StudentOut(BaseStudent):
    """Класс описывает студента, для отправления пользователю"""

    ID :uuid.UUID

class StudentStorage(BaseStudent):
    """Класс описывает хранимого студента в хранилище"""

    ID :uuid.UUID
    login :str
    password :str