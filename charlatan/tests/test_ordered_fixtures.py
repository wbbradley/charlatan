from __future__ import absolute_import

from charlatan import testing
from charlatan import FixturesManager


class TestOrderedixtures(testing.TestCase):

    def test_get_list_by_name(self):
        """Assert Charlatan loads its dependencies before loading the actual fixture"""
        fm = FixturesManager()
        def echo():
            print 'hey'
        fm.set_hook('before_install', echo)
        fm.load('./charlatan/tests/data/ordered_dependencies.yaml')
        # fixture = fm.get_fixture('fixture3')
        fixture = fm.install_fixture('fixture3')
        print 'zzz', fixture