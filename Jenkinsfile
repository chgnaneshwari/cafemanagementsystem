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
                    // Set up Python environment
                    sh '''
                        python -m venv venv  # Create a virtual environment
                        source venv/bin/activate  # Activate the virtual environment
                        pip install -r requirements.txt  # Install dependencies
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
    }
}
