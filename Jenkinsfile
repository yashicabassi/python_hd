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
                    // Run the Python tests using sh for macOS/Unix systems
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
                    // Run the Python app using sh for macOS/Unix systems
                    def result = sh(returnStatus: true, script: 'python3 app.py')
                    if (result != 0) {
                        error "Deployment failed"
                    }
                }
            }
        }
    }
}
