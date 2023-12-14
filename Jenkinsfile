pipeline {
  agent any
  stages {
    stage('Checking out code') {
      steps {
        git(url: 'https://github.com/tobsen666/literate-succotash', branch: 'main')
      }
    }

    stage('Build .dll') {
      steps {
        bat 'build-dll'
      }
    }

    stage('Pytest') {
      steps {
        bat 'pytest --html=report.html test_script.py > pytest_output.log 2>&1'
      }
    }

  }
}
