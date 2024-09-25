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
                // Use python3 directly instead of sh
                script {
                    def pythonTestCommand = 'python3 -m unittest test_app.py'
                    if (isUnix()) {
                        sh pythonTestCommand
                    } else {
                        bat pythonTestCommand
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                // Use python3 directly instead of sh
                script {
                    def pythonDeployCommand = 'python3 app.py'
                    if (isUnix()) {
                        sh pythonDeployCommand
                    } else {
                        bat pythonDeployCommand
                    }
                }
            }
        }
    }
}
