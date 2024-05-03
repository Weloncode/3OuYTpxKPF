
from facefusion import core

import getpass

from pyngrok import ngrok, conf

print("Enter your authtoken, which can be copied from https://dashboard.ngrok.com/auth")
conf.get_default().auth_token = "2fsCEZ7yGRcBnSsuX4iRRintOJ7_7254e3HQMifzNH8jFm2qQ"

# Open a TCP ngrok tunnel to the SSH server
connection_string = ngrok.connect("7860", "tcp").public_url

public_url = ngrok.connect(7860).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, 7860))


if __name__ == '__main__':
	core.cli()