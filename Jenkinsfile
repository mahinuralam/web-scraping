pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/TanjinAlam/fast-api-boilerplate', branch: 'dev')
      }
    }

    stage('Shell Script') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Shell Scritp') {
      steps {
        sh 'docker compose up --build'
      }
    }

  }
}
