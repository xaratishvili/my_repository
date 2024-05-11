class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = set()

    def create_post(self, content):
        post = Post(content, self)
        self.posts.append(post)
        return post

    def add_friend(self, friend):
        self.friends.add(friend)


class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []
        self.likes = 0

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self):
        self.likes += 1


class Comment:
    def __init__(self, content, author):
        self.content = content
        self.author = author


user1 = User("User1")
user2 = User("User2")


post1 = user1.create_post("This is a post by User1")
print(f"{user1.username} created a post: {post1.content}")

comment1 = Comment("This is a comment by User2 on post1", user2)
post1.add_comment(comment1)
print(f"{user2.username} commented on {user1.username}'s post: {comment1.content}")

post1.add_like()
print(f"{user1.username} liked {user2.username}'s comment on their post")

post2 = user1.create_post("This is another post by User1")
print(f"{user1.username} created another post: {post2.content}")

post2.add_like()
print(f"{user2.username} liked {user1.username}'s second post")
