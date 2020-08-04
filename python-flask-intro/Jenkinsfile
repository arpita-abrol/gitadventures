pipeline {
    agent any

    stages {
        stage('Codestyle check') {
            steps {
                echo 'Pycodestyle check...'
                sh "pycodestyle . || false"
            }
        }
        stage('Create Pipenv') {
            steps {
                echo 'Create Pipenv and install deps...'
                sh "python3.8 -m pip install pipenv"
		        sh "python3.8 -m pipenv install --dev"
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
		        sh "python3.8 -m pipenv run pytest -s tests || false"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
        stage('Clean Up') {
            steps {
                echo 'Remove venv...'
		        sh "python3.8 -m pipenv --rm"
            }
        }
    }
}
