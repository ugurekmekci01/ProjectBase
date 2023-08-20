pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // Replace this with your build commands
                sh 'echo "Building your project"'
            }
        }
        
        stage('Test') {
            steps {
                // Replace this with your test commands
                sh 'echo "Running tests"'
            }
        }
        
        stage('Deploy') {
            steps {
                // Replace this with your deployment commands
                sh 'echo "Deploying your project"'
            }
        }
    }
}
