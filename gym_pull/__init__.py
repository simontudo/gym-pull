import distutils.version
import logging

logger = logging.getLogger(__name__)


# Do this before importing any other gym modules, as most of them import some
# dependencies themselves.
def sanity_check_dependencies():
    import numpy
    import requests

    if distutils.version.LooseVersion(numpy.__version__) < distutils.version.LooseVersion('1.10.4'):
        logger.warn(
            "You have 'numpy' version %s installed, but 'gym' requires at least 1.10.4. HINT: upgrade via 'pip install -U numpy'.",
            numpy.__version__)

    if distutils.version.LooseVersion(requests.__version__) < distutils.version.LooseVersion('2.0'):
        logger.warn(
            "You have 'requests' version %s installed, but 'gym' requires at least 2.0. HINT: upgrade via 'pip install -U requests'.",
            requests.__version__)


sanity_check_dependencies()

from gym.core import Env, Space, Wrapper
from gym.envs import make, spec

import gym
import gym_pull.envs.registration

gym.envs.registration.env_id_re = gym_pull.envs.registration.env_id_re

logger.setLevel(logging.INFO)
from gym_pull.envs import list
from gym_pull.package import pull

__all__ = ["Env", "Space", "Wrapper", "list", "make", "pull", "spec", "upload"]
