pipeline {
    agent any
    
    environment {
        PYTHON = 'python'   // Windows Python command
        VENV = "${WORKSPACE}\\venv"
        APP_URL = 'http://staging.bank.local'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo "===== CHECKOUT CODE FROM GIT ====="
                checkout scm
                bat 'git log --oneline -5'
                bat 'git status'
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo "===== SETUP PYTHON ENVIRONMENT ====="
                bat '''
                    REM Create Python virtual environment
                    %PYTHON% -m venv %VENV%
                    call %VENV%\\Scripts\\activate
                    
                    REM Upgrade pip and install dependencies
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    
                    REM Create reports directory
                    if not exist reports mkdir reports
                    
                    echo Setup complete
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo "===== RUN PYTEST TESTS ====="
                bat '''
                    call %VENV%\\Scripts\\activate
                    
                    pytest tests/ ^
                        --html=reports\\report.html ^
                        --self-contained-html ^
                        --junitxml=reports\\junit.xml ^
                        -v
                '''
            }
        }
    }
    
    post {
        always {
            junit 'reports/junit.xml'
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Pytest Report'
            ])
        }
        success {
            echo "✓ Build Successful"
        }
        failure {
            echo "✗ Build Failed"
        }
    }
}
