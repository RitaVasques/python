import shop
import unittest
import datetime

class shopTests(unittest.TestCase):

    def setUp(self):
        self.cart = shop.ShoppingCart()
    
    def test_add_surfboards_one(self):
        self.assertEqual(self.cart.add_surfboards(1), "Successfully added 1 surfboard to cart!")
    
    # version with parametrization
    def test_add_sufboard(self):
        for i in range(2, 5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f"Successfully added {i} surfboards to cart!")
                self.cart = shop.ShoppingCart()

    # version no parametrization
    # def test_add_surfboards_two(self):
    #   self.assertEqual(self.cart.add_surfboards(2), "Successfully added 2 surfboards to cart!")

    @unittest.skip
    def test_too_many(self):
        self.assertRaises(shop.TooManyBoardsError, self.cart.add_surfboards, 5)

    # @unittest.expectedFailure (function is ok now)
    def test_local_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)
    
    def test_checkout_date(self):
        date = datetime.datetime.now()
        self.assertRaises(shop.CheckoutDateError, self.cart.set_checkout_date, date)

unittest.main()