pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ernes11to/jenkins_test'
            }
        }
        stage('Build and Test') {
            steps {
                sh 'docker build --no-cache -t jenkinsapp:latest .'
            }
        }
        stage('Push to Registry') {
            steps {
                sh 'docker tag jenkinsapp:latest 192.168.49.4:5000/jenkinsapp:latest'
                sh 'docker push 192.168.49.4:5000/jenkinsapp:latest'
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl --kubeconfig=/home/config apply -f k8s/'
                sh 'kubectl --kubeconfig=/home/config apply -rollout restart deployment flask-app'
            }
        }
        stage('Run End-to-End Tests') {
            steps {
                sh 'curl http://192.168.49.2:31000'
            }
        }
    }
    post {
        success {
            echo 'Pipeline ejecutado exitosamente.'
        }
        failure {
            echo 'Error en la ejecución del pipeline.'
        }
    }
}
