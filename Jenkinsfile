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
                echo 'Hello 2'
            }
        }
    }
}