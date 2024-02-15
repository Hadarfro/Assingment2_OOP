class SocialNetwork:

    active_network = None
    def __init__(self, nameNet):
        self.nameNet = nameNet
        self.users = []

        if not SocialNetwork.active_network:
            SocialNetwork.active_network = self.nameNet


    def sign_up(self, userName, password):
        self.users.append(userName, password)

        userName = input("enter your username: ")




    def log_in (self,  userName,  password):
         self.users(userName, password).isConnected()



    def log_out (self, userName):
        return False



