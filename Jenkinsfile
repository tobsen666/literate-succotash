pipeline {
    agent any
    stages {
        stage('Checking out code') {
            steps {
                echo 'Checking out code from the repository...'
                git(url: 'https://github.com/tobsen666/literate-succotash', branch: 'main')
            }
        }

        // Your other stages go here
    }

    // Post-build actions, etc.
}
