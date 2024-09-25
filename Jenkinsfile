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
                    if (isUnix()) {
                        // On Unix/macOS systems, execute Python test directly
                        echo "Running: python3 -m unittest test_app.py"
                        def result = sh(returnStatus: true, script: 'python3 -m unittest test_app.py')
                        if (result != 0) {
                            error "Unit tests failed"
                        }
                    } else {
                        // On Windows systems, use bat to run Python tests
                        echo "Running: python -m unittest test_app.py"
                        def result = bat(returnStatus: true, script: 'python -m unittest test_app.py')
                        if (result != 0) {
                            error "Unit tests failed"
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                script {
                    if (isUnix()) {
                        // On Unix/macOS systems, execute the Python app directly
                        echo "Running: python3 app.py"
                        sh 'python3 app.py'
                    } else {
                        // On Windows systems, use bat to run the Python app
                        echo "Running: python app.py"
                        bat 'python app.py'
                    }
                }
            }
        }
    }
}
