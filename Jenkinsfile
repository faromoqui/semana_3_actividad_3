pipeline {
    agent any

    environment {
        // Configura el entorno para enviar correos en caso de error
        EMAIL_RECIPIENTS = 'fa.ro.montenegro@unillanos.edu.co'        
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
                    def result = bat(script: 'python -m unittest discover -s test', returnStatus: true)
                    
                    // Verificar si los tests fallaron (código distinto de 0)
                    if (result != 0) {
                        currentBuild.result = 'FAILURE'
                        error('Tests fallaron')
                    }
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