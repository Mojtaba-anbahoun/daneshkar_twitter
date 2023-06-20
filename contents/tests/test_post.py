from django.test import TestCase
from contents.models import Post , Reaction , Comment
from accounts.models import User

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create()
        return super().setUp()
    
    def test_true_like(self):
        self.assertTrue(self.post.is_liked_by_user(user))

    def test_add_like(self):
        user = User.objects.create(username='moji')
        post = Post.objects.create(title='My Post', body='This is my post')
        like = post.add_like(user)
        self.assertIsInstance(like, Reaction)
        self.assertEqual(like.user, user)
        self.assertEqual(like.post, post)

    def test_remove_like(self):
        self.post.remove_like(self.user)
        self.assertFalse(Reaction.objects.filter(user=self.user, post=self.post).exists())

    def test_add_comment(self):
        comment = self.post.add_comment(self.user, 'This is a comment')
        self.assertEqual(Comment.objects.filter(user=self.user, post=self.post, text='This is a comment').count(), 1)
        self.assertEqual(comment.text, 'This is a comment')

    def test_get_comments(self):
        comments = self.post.get_comments()
        self.assertEqual(comments.count(), 2)
        self.assertEqual(comments[0], self.comment1)
        self.assertEqual(comments[1], self.comment2)


