#################################################################################################################
# Name = Padraic Mannion
# Student number = 10340056
# versions =
#################################################################################################################

# The unittest library is used to perform the test cases.
# By using import* importing everything from the titanic.py class.

import unittest
from titanic import*

# test the changes functionality
# unittest runs the test cases for the class.  TestCase is a subclass of the unit test class.
# not survived = 0 survived = 1 for survival variable.  The testPrediction_percentage looks into
# lines 280-286 of titanic.py function to test the accuracy of the function.
# for x in range loops 100 times through the prediction in the 1st case that the prediction is greater
# than .80.  The 2nd tests for a larger value than what the prediction percentage will be but as it'seek
# asserting false it returns true because the prediction isn't greater than .89
class TitanicTest(unittest.TestCase):
    def testPrediction_percentage(self):
        X_train = titanic_df.drop('Survived',axis=1) # dataset without the survived column ie test
        Y_train = titanic_df['Survived']
        for x in range (100):
            self.assertTrue(0.80<get_prediction_percentage(X_train, Y_train))
            self.assertFalse(0.89<get_prediction_percentage(X_train, Y_train))
if __name__ == '__main__':
    unittest.main()