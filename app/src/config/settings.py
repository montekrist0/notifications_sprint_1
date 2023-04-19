from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

base_settings = [
    'components/common.py',
    'components/hosts.py',
    'components/database.py',
    'components/apps_middleware.py',
    'components/authorization.py',
    'components/templates.py',
]

include(*base_settings)
