#!/usr/bin/env python3
"""Module for testing the client module."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/orgs/testorg/repos"
            }
            test_client = GithubOrgClient("testorg")
            result = test_client._public_repos_url
            self.assertEqual(
                result,
                "https://api.github.com/orgs/testorg/repos"
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect
        from the chosen payload.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = "hello/world"
            test_client = GithubOrgClient('test')
            result = test_client.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method of GithubOrgClient."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up class for the integration test."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class after the integration test."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method with a license."""
        test_client = GithubOrgClient("google")
        self.assertEqual(
            test_client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
