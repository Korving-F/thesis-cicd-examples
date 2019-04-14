# Example-App for CI comparative analysis

This app and accompanying files were developed as part of the author's graduating thesis at the Estonian IT-College / TTÜ.
It is partly based on a Flask example application provided on the official documentation page and functions for illustrative purposes.

This is the public version of this repository with links to CI tools that have been set up on dedicated machines in the cloud.
There is a private version available as well that includes similiar results for tools like Jenkins, GitlabCI, TeamCity and integration with OpenCov.

It contains the following:

* Minimalistic Flask-based web service
* Tests for the exposed API / dummy static functions
* Dockerfile to build and run the service
* Pipeline definition files for subset of selected CI tools


## Test results / Badges

* [CircleCI](https://circleci.com): [![CircleCI](https://circleci.com/gh/Korving-F/thesis-cicd-examples/tree/master.svg?style=svg)](https://circleci.com/gh/Korving-F/thesis-cicd-examples/tree/master)

* [TravisCI](https://travis-ci.org): [![Build Status](https://travis-ci.org/Korving-F/thesis-cicd-examples.svg?branch=master)](https://travis-ci.org/Korving-F/thesis-cicd-examples) [![codecov](https://codecov.io/gh/Korving-F/thesis-cicd-examples/branch/master/graph/badge.svg)](https://codecov.io/gh/Korving-F/thesis-cicd-examples)

* [GitlabCI](https://about.gitlab.com/product/continuous-integration/), [Jenkins](http://jenkins.io) and [TeamCity](https://www.jetbrains.com/teamcity/) badges for privately hosted CI/CD servers. Coverage report was uploaded to privately hosted [OpenCov](https://github.com/danhper/opencov). 
Integration between [SonarQube](https://www.sonarqube.org/), [bandit](https://github.com/PyCQA/bandit), [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), [pylint](https://www.pylint.org) and a slightly older version of this repository's code was setup, represented by the QualityGate badge.
  <br>
  <img src="https://raw.githubusercontent.com/Korving-F/thesis-cicd-examples/master/images/sonarqube-badge.png" alt="Badges and SonarQube Integration" height="50%" width="50%">

## Sources
* https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example
* https://docs.pytest.org/en/latest/example/simple.html
* Run build steps through CircleCI API calls: https://circleci.com/docs/2.0/api-job-trigger/
