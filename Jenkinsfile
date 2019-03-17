pipeline {
  agent any
  environment {
    CNAME = "jenkins-cicd-container-$GIT_COMMIT"
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build -t $CNAME .'
      }
    }
    stage('Run') {
      steps {
        echo 'Running appliances'
        sh '''docker kill $(docker ps -q) || true
              docker rm $(docker ps -a -q) || true
              docker run -dt -p 8282:80 -v $PWD:/tmp/ --name jenkinsCICDContainer $CNAME'''
      }
    }
    stage('Test') {
      steps {
        echo 'Testing...'
        sh '''sudo apt-get update -qy
	      sudo apt-get install -y python3-dev python3-pip
	      sudo pip3 install pytest pytest-cov
	      pytest --cov-report xml --cov-report term --cov-branch --cov=example/ tests/'''
      }
    }
    stage('Deploy') {
      when {
        expression {
	  currentBuild.result == null || currentBuild.result == 'SUCCESS'
	}
      }
      steps {
        echo 'Deploying...'
      }
    }
    stage('Clean') {
      steps {
        echo 'Cleaning up...'
        sh '''docker kill $(docker ps -q) || true
	      docker rm $(docker ps -a -q) || true'''
      }
    }
  }
}

