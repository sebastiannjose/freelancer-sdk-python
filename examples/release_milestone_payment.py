from freelancersdk.resources.projects import release_milestone_payment
from freelancersdk.session import Session
from freelancersdk.exceptions import MilestoneNotReleasedException
import os


# https://www.freelancer.com/api/docs/use-cases/milestone-actions
def sample_release_milestone_payment():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')

    session = Session(oauth_token=oauth_token, url=url)
    milestone_data = {
        'milestone_id': 1,
        'amount': 10,
    }
    try:
        m = release_milestone_payment(session, **milestone_data)
    except MilestoneNotReleasedException as e:
        print(('Error message: %s' % e.message))
        print(('Server response: %s' % e.error_code))
        return None
    else:
        return m


m = sample_release_milestone_payment()
if m:
    print(("Milestone released: %s" % m))
