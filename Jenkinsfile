pipeline {
    agent any
    stages {
        stage('Debug Shell') {
            steps {
                echo 'Checking shell environment...'
                script {
                    // Print the current shell being used and verify bash/sh availability
                    sh 'echo "Shell in use: $SHELL"'
                    sh 'which bash'
                    sh 'which sh'
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Python app...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                script {
                    def result = sh(returnStatus: true, script: 'python3 -m unittest test_app.py')
                    if (result != 0) {
                        error "Unit tests failed"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                script {
                    def result = sh(returnStatus: true, script: 'python3 app.py')
                    if (result != 0) {
                        error "Deployment failed"
                    }
                }
            }
        }
    }
}
