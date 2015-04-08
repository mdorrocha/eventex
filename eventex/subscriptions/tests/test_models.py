# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='21-96186180'
        )

    def test_unicode(self):
        self.assertEqual(u'Henrique Bastos', unicode(self.obj))

    def test_create(self):
        'Subscription must have name, cpf, email, phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        # Create a first entry to force the collision
        Subscription.objects.create(name='Henrique Bastos',
                                cpf='12345678901',
                                email='henrique@bastos.net',
                                phone='21-96186180')
    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name='Henrique Bastos',
                         cpf='12345678901',
                         email='outro@email.com',
                         phone='21-96186180')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Henrique Bastos',
                         cpf='00000000011',
                         email='henrique@bastos.net',
                         phone='21-96186180')
        self.assertRaises(IntegrityError, s.save)

