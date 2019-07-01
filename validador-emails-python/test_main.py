from main import filter_email
import unittest


class EmailValidTests(unittest.TestCase):
    def test_one(self):
        emails = [
            'lara@codenation.com',
            'brian-23@codenation.com.br',
            'britts_54@codenation.com'
        ]
        self.assertEqual(len(filter_email(emails)), 3)

    def test_two(self):
        emails = [
            'lara@gmail',
            'brian-23@codenation.br'
        ]
        self.assertEqual(len(filter_email(emails)), 1)

    def test_three(self):
        emails = [
            'dheeraj-234@gmail.com',
            'itsallcrap',
            'harsh_1234@red2iff.in',
            'kunal_shin@iop.az',
            'matt23@@india.in'
        ]
        self.assertEqual(len(filter_email(emails)), 3)

    def test_four(self):
        emails = [
            'fjladfk_iasdfad234@sdlkjf23335.in',
            'ha@git@int.cz',
            'prashant24_@gmail.com'
        ]
        self.assertEqual(len(filter_email(emails)), 2)

    def test_five(self):
        emails = [
            '',
            '@.com'
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_six(self):
        emails = [
            'pras#hant24_@gmail.com',
            'prashant24_@gmai$l.com',
            'prashant24_@gmail.co)m',
            'prashant24_@gmail.c(om',
            'prashant24_@gmai+l.com',
            'prashant24_@g/mail.com',
            'prashant24_@gmai*l.com',
            'prashant24_@gmail-com',
            'prasha@nt24_@gmail.com',
            'prashant24_@gmai#l.com',
            'prashant24_#gmail.com',
            'pra[shant24_@gmail.com.br',
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_seven(self):
        emails = [
            'prashant24_@gmail.co%m',
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_eight(self):
        emails = [
            'prashant24_@gmail.com#br',
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_nine(self):
        emails = [
            'prashant24_@gmail.com_br',
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_ten(self):
        emails = [
            'prashant24_@gma-il.com',
        ]
        self.assertEqual(len(filter_email(emails)), 0)

    def test_eleven(self):
        emails = [
            'prashant24_@a.com'
        ]
        self.assertEqual(len(filter_email(emails)), 1)

    def test_twelve(self):
        emails = [
            'prashant24_@a.b.c',
            'prashant24_@aa.bb.cc',
            'prashant24_@aaa.bbb.ccc',
        ]
        self.assertEqual(len(filter_email(emails)), 3)

    def test_extensao_caractere_max(self):
        emails = [
            'prashant24_@aaaaaaa.bbbvb.caaa',
            'prashant24_@aaaaaaa.bbb.aaac',
            'prashant24_@aaaaaaa.bbb',
            'prashant24_@aaaaaaa.bb',
            'prashant24_@aaaaaaa.b',
        ]
        self.assertEqual(len(filter_email(emails)), 3)


if __name__ == '__main__':
    unittest.main()
