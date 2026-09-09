pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/SHAH8860/python_file_Upload.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install fastapi uvicorn sqlalchemy pydantic[email] python-multipart'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Check Project') {
            steps {
                bat 'python -m py_compile main.py'
            }
        }
    }
}