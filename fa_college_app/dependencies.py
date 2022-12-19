from fa_college_app.repositories.group import GroupCSVRepository

REPOSITORY = GroupCSVRepository()

def get_group_repo() -> GroupCSVRepository:
    """Получение Group репозитория"""
    
    return REPOSITORY