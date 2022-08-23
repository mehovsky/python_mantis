from model.project import Project
import random
import string


def random_string(max_len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))]).rstrip()


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create_new_project(Project(project_name='Test', project_description='Test'))
    app.project.go_to_manage_projects()
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.project_name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.sort_by_name) == sorted(new_projects, key=Project.sort_by_name)