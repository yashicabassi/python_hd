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
                // Run the Python unittest without using 'sh'
                script {
                    if (isUnix()) {
                        // On Unix/macOS systems, use python3 directly
                        def pythonCommand = "python3 -m unittest test_app.py"
                        echo "Running: ${pythonCommand}"
                        def result = sh(script: pythonCommand, returnStatus: true)
                        if (result != 0) {
                            error "Unit tests failed"
                        }
                    } else {
                        // On Windows systems, use bat to run Python
                        def pythonCommand = "python -m unittest test_app.py"
                        echo "Running: ${pythonCommand}"
                        def result = bat(script: pythonCommand, returnStatus: true)
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
                // Run the Python app directly without using 'sh'
                script {
                    if (isUnix()) {
                        // On Unix/macOS systems, use python3 directly
                        def pythonCommand = "python3 app.py"
                        echo "Running: ${pythonCommand}"
                        sh pythonCommand
                    } else {
                        // On Windows systems, use bat to run Python
                        def pythonCommand = "python app.py"
                        echo "Running: ${pythonCommand}"
                        bat pythonCommand
                    }
                }
            }
        }
    }
}
