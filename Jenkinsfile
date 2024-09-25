pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the Python app...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                script {
                    // Run python3 for unit tests directly
                    def result = 'python3 -m unittest test_app.py'.execute()
                    result.waitFor()
                    echo result.text
                    if (result.exitValue() != 0) {
                        error "Unit tests failed"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                script {
                    // Run python3 for the app directly
                    def result = 'python3 app.py'.execute()
                    result.waitFor()
                    echo result.text
                    if (result.exitValue() != 0) {
                        error "Deployment failed"
                    }
                }
            }
        }
    }
}
