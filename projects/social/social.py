import random
import sys
sys.path.append('../graph')
from graph import Graph
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # self.vertices = {}

    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     s = Stack()
    #     visited = set()
    #     s.push([starting_vertex])
    #     while s.size() > 0:
    #         path = s.pop()
    #         vertex = path[-1]
    #         if vertex == destination_vertex:
    #             return path
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             for new_vert in self.friendships[vertex]:
    #                 new_path = path[:]
    #                 new_path.append(new_vert)
    #                 s.push(new_path)
    #     return visited

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                # print(v)
                visited.add(v)
                for next_vert in self.friendships[v]:
                    q.enqueue(next_vert)

        return v

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        # print([starting_vertex])
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            # print(vertex)
            if vertex == destination_vertex:
                return path
            if vertex not in visited:
                visited.add(vertex)
                for new_vert in self.friendships[vertex]:
                    new_path = path[:]
                    new_path.append(new_vert)
                    q.enqueue(new_path)
        return visited

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # def populate_graph(self, num_users, avg_friendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments

    #     Creates that number of users and a randomly distributed friendships
    #     between those users.

    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph
    #     self.last_id = 0
    #     self.users = {}
    #     self.friendships = {}
    #     # !!!! IMPLEMENT ME

    #     # Add users

    #     # Create friendships
    def populate_graph(self, num_users, avg_friendships):
     # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Friendships
        # Generate all possible friendship combinations
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        return self.friendships


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        friends_friends = []
        visited[user_id] = [user_id]

        for friend in self.friendships[user_id]:
            visited[friend] = self.bfs(user_id, friend)
            friends_friends.append(friend)

        while len(friends_friends) != 0:
            for friends in self.friendships[friends_friends[0]]:
                if friends not in friends_friends:
                    if friends not in visited:
                        friends_friends.append(friends)
                if friends not in visited:
                    visited[friends] = self.bfs(user_id, friends)
                    if friends not in friends_friends:
                        friends_friends.append(friends)
                if len(friends_friends) > 0:
                    friends_friends.pop(0)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
