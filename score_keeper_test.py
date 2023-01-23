from unittest import TestCase

from score_keeper import ScoreKeeper

class TestScoreKeeper(TestCase):
    def test_create_score_keeper(self):
        score_keeper = ScoreKeeper()
        self.assertEqual(score_keeper.getScore(), 0)