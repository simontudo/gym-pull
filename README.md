# gym-pull
#### **Gym Pull is an add-on for OpenAI Gym that allows the automatic downloading of user environments.**

Thanks a lot to ppaquette for coding this. Since his repository is no longer maintained, I forked it and made it compatible with the current version of gym. 

---
- [Installation](#installation)
- [Basic Usage](#basic_usage)
- [Listing Installed Environments](#listing_installed)

<div id="installation"></div>Installation
============

clone the repository: 

	git pull https://github.com/simontudo/gym-pull.git
	cd gym-pull
	pip install -e .

To run the add-on, you need to import gym, and then gym-pull:

.. code:: python

	  import gym
	  import gym_pull

<div id="basic_usage"></div>Basic Usage
======

The basic syntax for pulling a user environment is

.. code:: python

	  import gym
	  import gym_pull
	  gym_pull.pull('github.com/github_username/github_repo')

The repo github_username/github_repo must be a valid pip package.

Alternatively, you can

- specify a branch, tag, or commit using the "@" syntax. ``gym_pull.pull('github.com/username/repo@branch')``

The downloaded environment will be registered as ``USERNAME/ENV_NAME-vVERSION``. You can then make
the environment using the ``gym.make()`` command.

<div id="listing_installed"></div>Listing Installed Environments
======

You can list all installed environments by running ``gym_pull.list()``.

Alternatively, you can view all user environments installed by running
``[env for env in gym_pull.list() where '/' in env]``.
