// Jenkinsfile - Basic Configuration

pipeline {
    agent any
    
    environment {
        PYTHON = '/usr/bin/python3'
        VENV = "${WORKSPACE}/venv"
        APP_URL = 'http://staging.bank.local'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo "===== CHECKOUT CODE FROM GIT ====="
                checkout scm  // Automatically checks out from Git
                sh 'git log --oneline -5'
                sh 'git status'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo "===== SETUP PYTHON ENVIRONMENT ====="
                sh '''
                    # Install Chrome
                    apt-get update
                    apt-get install -y google-chrome-stable
                    
                    # Create Python virtual environment
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    
                    # Install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    # Create directories
                    mkdir -p reports
                    
                    echo "✓ Setup complete"
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo "===== RUN PYTEST TESTS ====="
                sh '''
                    . ${VENV}/bin/activate
                    
                    pytest tests/ \
                        --html=reports/report.html \
                        --self-contained-html \
                        --junitxml=reports/junit.xml \
                        -v
                '''
            }
        }
    }
    
    post {
        always {
            echo "===== PUBLISH RESULTS ====="
            
            junit 'reports/junit.xml'
            
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest Report',
                keepAll: true
            ])
            
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
        
        success {
            echo "✓ Build Successful"
        }
        
        failure {
            echo "✗ Build Failed"
        }
    }
}
