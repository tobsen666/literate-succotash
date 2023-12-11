pipeline {
  agent any
  stages {
    stage('Build .dll') {
      steps {
        sh 'gcc -shared -o addition.dll addition.c'
      }
    }

  }
}