# App configuration file
# Copy this file and rename it to 'app_config.py'
import os

# Flask App Configurations
flask_config = {

    # DEBUG mode only when developing on local server
    'DEBUG': True if os.getenv('SERVER_SOFTWARE', '').startswith('Development/') else False,

    # Flask uses this for cryptographic components
    'SECRET_KEY': 'Some big sentence',

}
