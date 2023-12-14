pipeline {
    agent any
    stages {
        stage('Checking out code') {
            steps {
                git(url: 'https://github.com/tobsen666/literate-succotash', branch: 'main')
            }
        }
    }
}
