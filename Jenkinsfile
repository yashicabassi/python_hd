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
                sh 'python3 -m unittest test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                sh 'python3 app.py'
            }
        }
    }
}
