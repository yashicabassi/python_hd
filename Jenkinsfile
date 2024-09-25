ppipeline {
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
                    // Use bash instead of sh for running commands
                    def result = bash(returnStatus: true, script: 'python3 -m unittest test_app.py')
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
                    // Use bash instead of sh for deployment
                    def result = bash(returnStatus: true, script: 'python3 app.py')
                    if (result != 0) {
                        error "Deployment failed"
                    }
                }
            }
        }
    }
}
