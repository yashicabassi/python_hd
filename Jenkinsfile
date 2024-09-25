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
                    // Directly run the Python command using Groovy's execute method
                    def testProcess = "python3 -m unittest test_app.py".execute()
                    testProcess.waitFor()
                    def output = testProcess.in.text
                    def errorOutput = testProcess.err.text

                    // Print output and error
                    echo output
                    if (errorOutput) {
                        error "Unit tests failed: ${errorOutput}"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python app...'
                script {
                    // Directly run the Python deployment command using Groovy's execute method
                    def deployProcess = "python3 app.py".execute()
                    deployProcess.waitFor()
                    def output = deployProcess.in.text
                    def errorOutput = deployProcess.err.text

                    // Print output and error
                    echo output
                    if (errorOutput) {
                        error "Deployment failed: ${errorOutput}"
                    }
                }
            }
        }
    }
}
