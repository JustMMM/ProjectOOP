from domain.models.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.database.orm import UserORM
from sqlalchemy.orm import Session
from typing import List

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[User]:
        return [User(id=u.id, username=u.username, email=u.email) for u in self.session.query(UserORM).all()]

    def get_by_id(self, user_id: int) -> User:
        u = self.session.query(UserORM).get(user_id)
        return User(id=u.id, username=u.username, email=u.email)

    def create(self, user: User) -> User:
        u = UserORM(username=user.username, email=user.email)
        self.session.add(u)
        self.session.commit()
        return User(id=u.id, username=u.username, email=u.email)