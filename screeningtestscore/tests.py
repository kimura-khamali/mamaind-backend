from django.test import TestCase
from django.contrib.auth import get_user_model  # To create a User instance
from mother.models import Mother
from community_health_promoter.models import CHP
from screeningtestscore.models import ScreeningTestScore
from datetime import date
from django.core.exceptions import ValidationError


class ScreeningTestScoreModelTest(TestCase):
    def setUp(self):
        """
        Set up the User, Mother, and CHP instances for the ScreeningTestScore model.
        """
        # Create a valid User instance
        self.user = get_user_model().objects.create_user(
            username="chpuser", email="chpuser@example.com", password="password123"
        )

        # Create Mother instance
        self.mother = Mother.objects.create(
            first_name="Jane",
            last_name="Doe",
            date_of_birth="1980-05-15",
            no_of_children=2,
            date_of_reg="2023-01-01",
            tel_no="123-456-7890",
            marital_status="Married",
            sub_location="SubLocation1",
            village="Village1",
        )

        # Create CHP instance, assigning a User instead of a Mother
        self.chp = CHP.objects.create(
            user=self.user,  # Must be a User instance
            registered_date="2023-01-01",
            reg_no="CHP123",
            phone_number="1234567890",
            location="Location1",
            sub_location="SubLocation1",
            village="Village1",
        )

    def test_screening_test_score_creation(self):
        """
        Happy path: Test if the ScreeningTestScore instance is created successfully.
        """
        screening_test = ScreeningTestScore.objects.create(
            mother=self.mother, chp=self.chp, test_date=date.today(), total_score=10
        )

        self.assertEqual(screening_test.mother, self.mother)
        self.assertEqual(screening_test.chp, self.chp)
        self.assertEqual(screening_test.total_score, 10)
        self.assertIsInstance(screening_test.test_date, date)
        self.assertEqual(
            str(screening_test),
            f"Test {screening_test.test_id} - Total Score: {screening_test.total_score}",
        )


class ScreeningTestScoreModelUnhappyPathTest(TestCase):
    def setUp(self):
        """
        Set up the User, Mother, and CHP instances for the ScreeningTestScore model.
        """
        # Create a valid User instance
        self.user = get_user_model().objects.create_user(
            username="chpuser", email="chpuser@example.com", password="password123"
        )

        # Create Mother instance
        self.mother = Mother.objects.create(
            first_name="Jane",
            last_name="Doe",
            date_of_birth="1980-05-15",
            no_of_children=2,
            date_of_reg="2023-01-01",
            tel_no="123-456-7890",
            marital_status="Married",
            sub_location="SubLocation1",
            village="Village1",
        )

        # Create CHP instance, assigning a User instead of a Mother
        self.chp = CHP.objects.create(
            user=self.user,  # Must be a User instance
            registered_date="2023-01-01",
            reg_no="CHP123",
            phone_number="1234567890",
            location="Location1",
            sub_location="SubLocation1",
            village="Village1",
        )

    def test_missing_total_score(self):
        """
        Unhappy path: Test that missing total_score raises a ValidationError.
        """
        screening_test = ScreeningTestScore(
            mother=self.mother,
            chp=self.chp,
            test_date=date.today(),
            total_score=None,  # Missing total_score
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError

    def test_negative_total_score(self):
        """
        Unhappy path: Test that a negative total_score raises a ValidationError.
        """
        screening_test = ScreeningTestScore(
            mother=self.mother,
            chp=self.chp,
            test_date=date.today(),
            total_score=-5,  # Invalid negative score
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError

    def test_missing_mother(self):
        """
        Unhappy path: Test that missing mother raises a ValidationError.
        """
        screening_test = ScreeningTestScore(
            mother=None,  # Missing mother
            chp=self.chp,
            test_date=date.today(),
            total_score=10,
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError

    def test_missing_chp(self):
        """
        Unhappy path: Test that missing CHP raises a ValidationError.
        """
        screening_test = ScreeningTestScore(
            mother=self.mother,
            chp=None,  # Missing CHP
            test_date=date.today(),
            total_score=10,
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError

    def test_missing_test_date(self):
        """
        Unhappy path: Test that missing test_date raises a ValidationError.
        """
        screening_test = ScreeningTestScore(
            mother=self.mother,
            chp=self.chp,
            test_date=None,  # Missing test_date
            total_score=10,
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError

    def test_future_test_date(self):
        """
        Unhappy path: Test that a future test_date raises a ValidationError.
        """
        future_date = date(
            2100, 1, 1
        )  # Future date is invalid (depending on business rules)
        screening_test = ScreeningTestScore(
            mother=self.mother,
            chp=self.chp,
            test_date=future_date,  # Invalid future date
            total_score=10,
        )
        with self.assertRaises(ValidationError):
            screening_test.full_clean()  # This should raise a ValidationError
