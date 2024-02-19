

class Users:
    followers = []
    posts = []
    notification = []
    isConnected = False
    name = None
    password = None

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.isConnected = True

    def follow(self, user):
        if self.isConnected:
            self.followers.append(user)
            print("Follow succeeded")

    def unfollow(self, user):
        if self.isConnected:
            self.followers.remove(user)
            print("Unfollow succeeded")

    def publish_post(self, type_post, *content):  # using factory
        if self.isConnected:
            post = Posts.create_post(type_post, Users(self.name, self.password), *content)
            return post

    @staticmethod
    def update(message):
        print(f"{message}")

    def notify(self, new_post):
        print("Received a notification for a new post")
        for follower in self.followers:
            follower.update(f"{self.name} published a post {new_post}")

    @staticmethod
    def print_info(self, user):
        print(f"Followers: {user.followers}")
        print(f"Posts: {user.posts}")
        print(f"Notification: {user.notification}")

    def print_notifications(self):
        for notif in reversed(self.notification):
            print(notif)


