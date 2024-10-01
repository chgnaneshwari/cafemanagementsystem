pipeline {
    agent any 

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/chgnaneshwari/cafemanagementsystem.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    // Check if the virtual environment exists
                    if (!fileExists('venv')) {
                        // Set up Python environment
                        sh '''
                            python -m venv venv  # Create a virtual environment
                        '''
                    }
                    // Activate the virtual environment and install dependencies
                    sh '''
                        source venv/bin/activate  # Activate the virtual environment
                        pip install flask pytest  # Install specific dependencies
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add any build steps if necessary
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh '''
                        source venv/bin/activate  # Activate virtual environment
                        pytest  # Running tests using pytest
                        deactivate  # Deactivate the virtual environment
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            // Optionally clean up resources or send notifications
            echo 'Cleaning up...'
            sh 'rm -rf venv' // Remove the virtual environment if needed
        }
    }
}
