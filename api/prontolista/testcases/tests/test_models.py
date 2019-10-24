from django.test import TestCase

from model_mommy import mommy

from projects.models import Project
from ..models import TestCase as TestCaseModel


class TestCaseModelTest(TestCase):
    def test_model_should_have_name(self):
        project = mommy.make(Project)
        expected_name = "Breadcrumb : click breadcrumb link"
        actual = TestCaseModel.objects.create(name=expected_name, project=project)

        assert actual.name == expected_name
        assert actual.created
        assert actual.modified

    def test_model_should_have_foreign_key_to_project(self):
        expected_project_name = "Gravity Form test"
        project = mommy.make(Project, name=expected_project_name)
        actual = TestCaseModel.objects.create(name="breadcrumb test", project=project)

        assert actual.project.name == expected_project_name
        assert actual.created
        assert actual.modified
