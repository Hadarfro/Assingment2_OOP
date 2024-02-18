from abc import abstractmethod
from Posts import Posts
from SocialNetwork import SocialNetwork

class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.isConnected = False

    def follow(self, user):
        pass

    def unfollow(self, user):
        pass

    def publish_post(self, typePost, *content): # using factory
        post = Posts.create_post(typePost, *content)
        return post

    def notify(self):
        pass

    def printInfo(self):
        pass

    def printNotifaction(self):
        pass

