from enum import Enum
from abc import ABC, abstractmethod

class PostType(Enum):
    TextPost = "textPost"
    ImagePost = "imagePost"
    SalePost = "salePost"

class Type(ABC):
    @abstractmethod
    def like(self,user): # continue
        pass

    def comment(self,user, content):
        pass
    def printInfo(self, user):
        pass

class Posts:
    likeCount = 0
    comments = []
    owner = None
    def create_post(self, post_type, content):
        if post_type == post_type.TEXTPOST:
            return TextPost()
        elif post_type == post_type.IMAGEPOST:
            return ImagePost()
        elif post_type == post_type.SALEPOST:
            return SalePost()
        else:
            raise ValueError("Invalid post type")
