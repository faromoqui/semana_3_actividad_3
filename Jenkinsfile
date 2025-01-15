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
         stage('compilaccion') {
            steps {
                def result = bat(script: 'python -m unittest discover -s tests', returnStatus: true)

                    // Si el resultado es distinto de 0, significa que los tests fallaron
                    if (result != 0) {
                        currentBuild.result = 'FAILURE'
                        error('Tests fallaron')
                    }
            }
        }
    }
    post {
        success {
            // Enviar mensaje si los tests pasaron
            echo 'Todos los tests pasaron con éxito.'
        }
        failure {
            // Enviar correo si los tests fallaron
            emailext (
                subject: "Fallo en el pipeline de Jenkins - Tests fallidos",
                body: "Los tests de Python han fallado en la ejecución del pipeline de Jenkins. Revisa el reporte para más detalles.",
                to: "${EMAIL_RECIPIENTS}"
            )
        }
    }
}