from fastapi import APIRouter, Depends
from fa_college_app.dependencies import get_group_repo
from fa_college_app.models.group import GroupOut, GroupIn, GroupStorage
from fa_college_app.repositories.group import BaseGroupRepository
from typing import List


router = APIRouter()

@router.post("/group", response_model = GroupOut)
def create_group(
    group_in :GroupIn,
    group_repo :BaseGroupRepository = Depends(get_group_repo)
    ):
    return group_repo.create(group_in)

@router.get("/group", response_model = GroupOut)
def get_by_id(
    id: int,
    group_repo :BaseGroupRepository = Depends(get_group_repo),
    ):
    return group_repo.get_by_id(id=id)

@router.get("/groups", response_model= List[GroupOut])
def get_all(
    limit :int,
    skip :int,
    group_repo :BaseGroupRepository = Depends(get_group_repo)
    ):
    return group_repo.get_all(limit=limit, skip=skip)