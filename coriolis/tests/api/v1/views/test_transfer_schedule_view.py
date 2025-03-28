# Copyright 2023 Cloudbase Solutions Srl
# All Rights Reserved.

from coriolis.api.v1.views import transfer_schedule_view
from coriolis.tests import test_base


class TransferViewTestCase(test_base.CoriolisApiViewsTestCase):
    """Test suite for the Coriolis api v1 views."""

    def test_single(self):
        fun = getattr(transfer_schedule_view, 'single')
        self._single_view_test(fun, 'schedule')

    def test_collection(self):
        fun = getattr(transfer_schedule_view, 'collection')
        self._collection_view_test(fun, 'schedules')
