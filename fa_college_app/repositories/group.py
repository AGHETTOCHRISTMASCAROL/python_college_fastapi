from core import settings
from fa_college_app.models.group import GroupIn, GroupOut, GroupStorage
from typing import List
from fa_college_app.utils.repository_utils import convert_group_in_to_storage
import csv
import os


class BaseGroupRepository:
    """Базовый класс для реализации функционала работы с группами"""

    def get_by_id(self, id :int) -> GroupOut:
        raise NotImplementedError

    def get_all(self,) -> List[GroupOut]:
        raise NotImplementedError

    def create(self, group :GroupIn) -> GroupOut:
        raise NotImplementedError

    def update(self, id :int) -> GroupOut:
        raise NotImplementedError

    def delete(self, id :int):
        raise NotImplementedError

class GroupCSVRepository(BaseGroupRepository):
    """Реализация функционала для работы с группами в .csv хранилище"""
    
    def __init__(self,):
        with open(settings.PATH_DATABASE, "a+", newline="") as file:
            if os.stat(settings.PATH_DATABASE).st_size == 0:
                writer = csv.writer(file)
                writer.writerow(["id", "name"])

    def get_by_id(self, id :int) -> GroupOut:
        """Вывод группы по id"""

        with open(settings.PATH_DATABASE, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                if row["id"] == str(id):
                    return GroupOut(**row)
            return None

    def get_all(self, limit :int, skip :int) -> List[GroupOut]:
        """Вывод списка групп"""

        group_out_list :List[GroupOut] = []
        with open(settings.PATH_DATABASE, "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                group_out_list.append(GroupOut(**row))
        return group_out_list[skip:skip+limit]

    def create(self, group_in :GroupIn) -> GroupOut:
        """Для создания группы, хранимой в .csv и вывода GroupOut"""

        group_storage :GroupStorage = convert_group_in_to_storage(group_in)

        group_storage_dict :dict = group_storage.dict()
        with open(settings.PATH_DATABASE, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name'], delimiter=";")
            writer.writerow(group_storage_dict)
        return GroupOut(**group_storage_dict)

    def update(self, id :int) -> GroupOut:
        pass

    def delete(self, id :int):
        pass