
# Import Django's testing framework
from django.test import TestCase

# Import Django's built-in User model
from django.contrib.auth.models import User

# Import models used by the library application
from library.models import Book, Member, RFIDEvent

# Import services/functions that we want to test
from library.services import (
    RFIDReaderAdapter,
    GateAdapter,
    checkout
)


# ============================================================
# CORE SCENARIO TESTS
#
# TestCase provides an isolated test database for these tests.
# Django creates a temporary database when the tests run.
# ============================================================

class CoreScenarioTests(TestCase):


    # ========================================================
    # SETUP
    #
    # setUp() runs before every test method.
    #
    # It creates the sample data required by the tests.
    # ========================================================

    def setUp(self):

        # Create a test user
        self.u = User.objects.create_user(
            'tester',
            '',
            'pass'
        )


        # Create a synthetic library member
        self.m = Member.objects.create(
            card_no='M100',
            name='Synthetic User'
        )


        # Create a synthetic book with an RFID tag
        self.b = Book.objects.create(
            accession_no='B100',
            title='Synthetic Book',
            rfid_tag='TAG100'
        )


    # ========================================================
    # TEST 1: RFID READER
    #
    # Verifies that the RFID reader can successfully find
    # the RFID tag TAG100.
    # ========================================================

    def test_rfid_read(self):

        # Create the RFID reader adapter and read the tag
        result = RFIDReaderAdapter().read('TAG100')


        # Verify that the RFID tag was found
        self.assertTrue(
            result['found']
        )


    # ========================================================
    # TEST 2: BOOK CHECKOUT
    #
    # Verifies that the checkout service changes the
    # book status to ISSUED.
    # ========================================================

    def test_checkout(self):

        # Perform checkout using:
        # Book → self.b
        # Member → self.m
        # User → self.u
        checkout(
            self.b,
            self.m,
            self.u
        )


        # Refresh the book object from the database
        # so that we get its latest status.
        self.b.refresh_from_db()


        # Verify that the book status is now ISSUED
        self.assertEqual(
            self.b.status,
            'ISSUED'
        )


    # ========================================================
    # TEST 3: SECURITY GATE EVENT
    #
    # Verifies that the security gate adapter creates
    # an UNAUTHORIZED_REMOVAL event.
    # ========================================================

    def test_gate_event(self):

        # Simulate an unauthorized RFID gate event
        event = GateAdapter().emit_unauthorized(
            'TAG100',
            'B100'
        )


        # Verify that the generated event has the
        # expected event type.
        self.assertEqual(
            event.event_type,
            'UNAUTHORIZED_REMOVAL'
        )
