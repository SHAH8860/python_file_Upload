pipeline {
    agent any

    stages {

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'where python'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install fastapi uvicorn sqlalchemy pydantic[email] python-multipart'
            }
        }

        stage('Check Project') {
            steps {
                bat 'python -m py_compile main.py'
            }
        }
    }
}