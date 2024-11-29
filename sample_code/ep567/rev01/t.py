from sentry.buffer import backend
from sentry.models.group import Group
from sentry.models.organization import Organization
from sentry.models.project import Project
from sentry.models.release import Release
from sentry.models.releases.release_project import ReleaseProject
from sentry.models.team import Team


group = Group.objects.create(project=Project(id=1))
org = Organization.objects.create(slug="test-org")
team = Team.objects.create(organization=org, slug="test-team")
project = Project.objects.create(organization=org, slug="test-project")
project.add_team(team)
release = Release.objects.create(organization=org, version="abcdefg")
release_project = ReleaseProject.objects.create(project, release=release)

while True:
    columns = {"times_seen": 1}
    filters = {"id": group.id, "project_id": 1}
    backend.incr(Group, columns, filters)
