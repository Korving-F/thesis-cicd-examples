# Example-App for CI comparative analysis

This app and accompanying files were developed as part of the author's graduating thesis at the Estonian IT-College / TTÜ. 
It is partly based on a Flask example application provided on the official documentation page and functions for illustrative purposes.

This is the public version of this repository with links to CI tools that have been set up on dedicated machines. 
There is a private version available as well that includes similiar results for tools like Jenkins, GitlabCI, TeamCity and integration with OpenCov.

It contains the following:

* Minimalistic Flask-based web service
* Tests for the exposed API / dummy static functions
* Dockerfile to build and run the service
* Pipeline definition files for subset of selected CI tools


## Test results / Badges

* CircleCI: [![CircleCI](https://circleci.com/gh/Korving-F/thesis-cicd-examples/tree/master.svg?style=svg)](https://circleci.com/gh/Korving-F/thesis-cicd-examples/tree/master)

* TravisCI: [![Build Status](https://travis-ci.org/Korving-F/thesis-cicd-examples.svg?branch=master)](https://travis-ci.org/Korving-F/thesis-cicd-examples) [![codecov](https://codecov.io/gh/Korving-F/thesis-cicd-examples/branch/master/graph/badge.svg)](https://codecov.io/gh/Korving-F/thesis-cicd-examples)

## Sources
* https://flask-restful.readthedocs.io/en/latest/quickstart.html#full-example
* https://docs.pytest.org/en/latest/example/simple.html
