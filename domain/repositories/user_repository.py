from abc import ABC, abstractmethod
from domain.models.user import User
from typing import List

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[User]: pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User: pass

    @abstractmethod
    def create(self, user: User) -> User: pass