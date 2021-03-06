import pytest
from cc2olx.link_file_reader import LinkFileReader


@pytest.fixture(scope="session")
def link_map(link_map_csv):
    link_map = LinkFileReader(link_map_csv).get_link_map()
    return link_map


class TestLinkMapReader:
    def test_link_map_generation(self, link_map):
        """
            Test if the all the data from the file is read.

        Args:
            link_map ([fixture]): Map of links to rows
        """
        assert len(link_map) == 5

    def test_link_map_value(self, link_map):
        """
            Ensure that the links are forming the right map.
        Args:
            link_map ([fixture]): Map of links to rows
        """
        assert link_map[
            "https://cdnapisec.kaltura.com/p/2019031/sp/201903100/playManifest/entryId/1_9if7cth0/format/url/protocol/https"  # noqa: E501
        ] == {
            "Edx Id": "42d2a5e2-bced-45d6-b8dc-2f5901c9fdd1",
            "External Video Link": "https://cdnapisec.kaltura.com/p/2019031/sp/201903100/playManifest/entryId/1_9if7cth0/format/url/protocol/https",  # noqa: E501
            "Youtube Id": "NXlG00JYX-o",
        }

    def test_read_csv_file(self, link_map_csv):
        """
            Test the read csv file.
        Args:
            link_map_csv ([str]): The file path for the csv file.
        """
        rows = LinkFileReader(link_map_csv)._read_csv_file()
        assert len(rows) == 5
