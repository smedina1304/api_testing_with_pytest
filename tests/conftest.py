import pytest


def pytest_html_report_title(report):
    ''' modifying the title of html report'''
    report.title = "My very own title!"