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
                script {
                    // Ejecutar los tests utilizando unittest y capturar el resultado
                    // Utilizando returnStatus para capturar el código de salida sin necesidad de 'def'
                    def result = bat(script: 'python -m unittest discover -s tests', returnStatus: true)
                    
                    // Verificar si los tests fallaron (código distinto de 0)
                    if (result != 0) {
                        currentBuild.result = 'FAILURE'
                        error('Tests fallaron')
                    }
                }
            }
        }
    }
    
}