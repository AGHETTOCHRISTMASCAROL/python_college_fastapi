from time import time
from fa_college_app.models.group import GroupIn, GroupStorage

def gen_id():
    while True:
        yield int(time() * 1000)

def convert_group_in_to_storage(group: GroupIn) -> GroupStorage:
    """Конвертирует из класса GroupIn >> GroupStorage"""

    temp_dict = group.dict()
    gen = gen_id()
    group_storage = GroupStorage(id=next(gen), **temp_dict)
    return group_storage