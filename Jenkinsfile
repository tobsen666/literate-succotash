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
        bat 'pytest --html=report.html addition_testing_c.py'

        // Capture the exit code of the Pytest command
        def result = bat(script: 'echo %ERRORLEVEL%', returnStatus: true)
            
        // Print the result to the Jenkins console
        echo "Pytest command exit code: ${result}"
      }
    }

  }
}
