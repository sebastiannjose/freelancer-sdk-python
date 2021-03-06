from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import get_projects
from freelancersdk.resources.projects.helpers import (
    create_get_projects_object, create_get_projects_project_details_object,
    create_get_projects_user_details_object
)
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
import os
import json


def sample_get_projects():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)

    query = create_get_projects_object(
        project_ids=[
            201,
            202,
            203,
        ],
        project_details=create_get_projects_project_details_object(
            full_description=True,
            jobs=True,
            qualifications=True,
        ),
        user_details=create_get_projects_user_details_object(
            basic=True,
            profile_description=True,
            reputation=True,
        ),
    )

    try:
        p = get_projects(session, query)
    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


p = sample_get_projects()
if p:
    print('Found projects: {}'.format(json.dumps(p)))
