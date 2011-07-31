"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class IndexViewTestCase(TestCase):
    fixtures = ['test_votes.json']

    def setUp(self):
        self.response = self.client.get('/')
        
    def test_index(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_show_owned_game(self):
        games = self.response.context['game_list']
        for g in games:
            self.assertTrue(g.owned)

    def test_index_show_sort_game(self):
        games = self.response.context['game_list']
        sorted_games = sorted(games)
        self.assertEqual(len(games), len(sorted_games))
        for i in range(len(games)):
            self.assertEqual(games[i], sorted_games[i])

    def test_index_template(self):
        template_names = [t.name for t in self.response.templates]
        self.assertEqual('index.html', template_names[0])

    def tearDown(self):
        del self.response

class WishesViewTestCase(TestCase):
    fixtures = ['test_votes.json']

    def setUp(self):
        self.response = self.client.get('/wishes/')

    def test_wishes(self):
        self.assertEqual(self.response.status_code, 200)

    def test_wishes_template(self):
        template_names = [t.name for t in self.response.templates]
        self.assertEqual('wishes.html', template_names[0])

    def test_wishes_sort_by_count(self):
        votes = self.response.context['vote_list']
        for i in range(len(votes) - 1):
            self.assertTrue(votes[i].count >= votes[i+1].count)
    
    def tearDown(self):
        del self.response

class OwnedViewTestCase(TestCase):
    fixtures = ['test_votes.json']
        
    def setUp(self):
        self.response = self.client.get('/owned/')

    def test_owned(self):
        self.assertEqual(self.response.status_code, 200)

    def test_owned_template(self):
        template_names = [t.name for t in self.response.templates]
        self.assertEqual('owned.html', template_names[0])

    def test_owned_sort_by_title(self):
        games = self.response.context['owned_list']
        sorted_games = sorted(games)
        self.assertEqual(len(games), len(sorted_games))
        for i in range(len(games)):
            self.assertEqual(games[i], sorted_games[i])

    def tearDown(self):
        del self.response

class RegisterViewTestCase(TestCase):
    pass

class AddGameViewTestCase(TestCase):
    pass

class ThumbUpViewTestCase(TestCase):
    pass
