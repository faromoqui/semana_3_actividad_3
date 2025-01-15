pipeline {
    agent any

    environment {
        // Configura el entorno para enviar correos en caso de error
        EMAIL_RECIPIENTS = 'fa.ro.montenegro@unillanos.edu.co'
        GITHUB_REPO_URL = 'https://github.com/tu_usuario/tu_repositorio.git' // Cambia esta URL por la de tu repositorio
    }
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('ejecutar test') {
            steps {
                bat 'python test_ejercicio.py'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                script {
                    // Instalar las dependencias, incluyendo Selenium
                    bat 'pip install selenium'
                }
            }
        }
        stage('compilaccion') {
            steps {
                def result = bat(script: 'python -m unittest discover -s test', returnStatus: true)
            }
        }
    }
    
}