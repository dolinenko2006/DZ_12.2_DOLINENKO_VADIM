import json

class PostHandler():
    def __int__(self, path):
        self.path = path

    def load_posts(self):
        posts = []
        try:
              with open (self, path, 'r', encoding='utf-8') as file:
                  posts = json.load(file)
        except Exception as e:
            print(f"ошибка загрузки {e}")
        return posts

    def search_posts (self, substr):
        posts =[]
        for posts in self.load_posts():
            if substr.lower() in post['content'].lower():
                posts.append(post)
        return posts


    def save_posts_to_json(self, posts):
        with open (self, path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)


    def add_post (self, post):
        posts = self.load_posts()
        post.append(post)
        self.save_posts_to_json(posts)