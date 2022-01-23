import unittest
from user import User


class TestUser(unittest.TestCase):
    """Test class that defines test cases for the user class behaviours."""

    def setUp(self):
        """setUp method to define instructions that will be executed before each test method."""
        self.new_user = User("David","David@")

    def tearDown(self):
        """tearDown method that does clean up after each test case has run."""

        User.user_list = []

    # First test--check if we can create users
    def test_init(self):
        """test_init test case to test if the object is initialized properly"""

        self.assertEqual(self.new_user.username,"David")
        self.assertEqual(self.new_user.password,"David@")

    # Second Test --- check if it can save users
    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the user list"""

        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    # Third Test --- check if it can save multiple users
    def test_save_multiple_users(self):
        """test_save_multiple_users to check if we can save multiple user objects to our user_list"""

        self.new_user.save_user()
        test_user = User("Mercy", "Mchelaa")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    if __name__ == "__main__":
        unittest.main()