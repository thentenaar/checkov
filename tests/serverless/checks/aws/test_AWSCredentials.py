import os
import unittest

from checkov.serverless.checks.function.aws.AWSCredentials import check
from checkov.serverless.runner import Runner
from checkov.runner_filter import RunnerFilter


class TestAWSCredentials(unittest.TestCase):

    def test_summary(self):
        runner = Runner()
        current_dir = os.path.dirname(os.path.realpath(__file__))

        test_files_dir = current_dir + "/example_AWSCredentials"
        report = runner.run(root_folder=test_files_dir, runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()

        self.assertEqual(summary['passed'], 1)
        self.assertEqual(summary['failed'], 2)
        self.assertEqual(summary['skipped'], 0)
        self.assertEqual(summary['parsing_errors'], 0)

        for failed_check in report.failed_checks:
            del failed_check.entity_tags['__file__']
            self.assertEqual(dict(sorted(failed_check.entity_tags.items())), {"RESOURCE": "lambda", "PUBLIC": "False"})


if __name__ == '__main__':
    unittest.main()
