## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url = '/lab'

## Configure authentication (delagated to GitLab)
from oauthenticator.gitlab import GitLabOAuthenticator
c.JupyterHub.authenticator_class = GitLabOAuthenticator
c.GitLabOAuthenticator.oauth_callback_url = 'http://localhost/hub/oauth_callback'
c.GitLabOAuthenticator.client_id = '27038842dc1108b3e57f8093f3d7af3dab658997ad796f4abb816ecd82ae6c73'
c.GitLabOAuthenticator.client_secret = '0600900be608f4c02bc349013f41e14d6b9f54afbe59c6ce3aa9de904a90781d'
c.Authenticator.admin_users = { 'studnitz' }


## Docker spawner
import os

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/joyvan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '1G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
