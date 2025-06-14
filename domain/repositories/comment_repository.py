from abc import ABC, abstractmethod
from typing import List
from domain.models.comment import Comment

class CommentRepository(ABC):
    @abstractmethod
    def get_all_by_post_id(self, post_id: int) -> List[Comment]: pass

    @abstractmethod
    def create(self, comment: Comment) -> Comment: pass