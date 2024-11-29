from sentry.buffer import backend
from sentry.models.group import Group
from sentry.models.project import Project

group = Group.objects.create(project=Project(id=1))
org = Organization.objects.create(slug="test-org")
team = Team.objects.create(organization=org, slug="test-team")
prject = Project.objects.create(organization=org, slug="test-project")
project.add_team(team)
release = Release.objects.create(organization=org, version="abcdefg")
release_project = ReleaseProject.objects.create(project, release=release)

while True:
    columns = {"times_seen": 1}
    filters = {"id": group.id, "project_id": 1}
    backend.incr(Group, columns, filters)
