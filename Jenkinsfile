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
        sh '''cd \${WORKSPACE}
        gcc -shared -o addition.dll add.c
        '''
      }
    }

  }
}
