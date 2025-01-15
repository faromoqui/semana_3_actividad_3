pipeline {
    agent any

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
}