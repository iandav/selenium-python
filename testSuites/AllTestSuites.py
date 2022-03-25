import unittest
from package1.TC_loginTest import LoginTest
from package1.TC_SignUpTest import SignUpTest
from package2.TC_paymentTest import PaymentTest
from package2.TC_reportTest import ReportTest

# Get all tests
tc1 = unittest.TestLoader.loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader.loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader.loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader.loadTestsFromTestCase(ReportTest)

# Create test suite
firstTS = unittest.TestSuite.addTests([tc1,tc2])

# Run tests
unittest.TextTestRunner.run()