# import csv
# import os
# from core import settings
# from typing import List
# from fa_college_app.models.group import GroupOut, GroupStorage

# group_out_list :List[GroupOut] = []

# with open(settings.PATH_DATABASE, 'r', newline="") as file:
#     pass
#     reader = csv.DictReader(file, delimiter=';')
#     for row in reader:
#         print(GroupOut(**row))

# with open(settings.PATH_DATABASE, "r") as file:
#     reader = csv.DictReader(file, delimiter=";")
#     for row in reader:
#         if row["id"] == '123':
#             group_out = GroupOut(**row)
# print(group_out)

# group_storage = {
#     'id': '123456',
#     'name': 'name123'
# }

# with open(settings.PATH_DATABASE, "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=['id', 'name'], delimiter=";")
#     writer.writerow(group_storage)

# with open(settings.PATH_DATABASE, "a+", newline="") as file:
#     if os.stat(settings.PATH_DATABASE).st_size == 0:
#         writer = csv.writer(file)
#         writer.writerow(['id', 'name'])