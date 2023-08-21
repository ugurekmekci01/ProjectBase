pipeline {
  agent any
  stages {
    stage('Extract') {
      parallel {
        stage('Extract') {
          steps {
            checkout scm
          }
        }

        stage('ExtOrac') {
          steps {
            sh 'sh /opt/jenkins_scripts/extract1.sh'
          }
        }

        stage('ExtOrac2') {
          steps {
            sh 'sh /opt/jenkins_scripts/extract2.sh'
          }
        }

        stage('ExtOrac3') {
          steps {
            sh 'sh /opt/jenkins_scripts/extract3.sh'
          }
        }

      }
    }

    stage('Transfrom') {
      parallel {
        stage('Transfrom') {
          steps {
            sh 'echo "Running Transformation Jobs"'
          }
        }

        stage('Transform 1') {
          steps {
            sh 'sh /opt/jenkins_scripts/transform1.sh'
          }
        }

        stage('Transform 2') {
          steps {
            sh 'sh /opt/jenkins_scripts/transform2.sh'
          }
        }

        stage('Transform3') {
          steps {
            sh 'sh /opt/jenkins_scripts/transform3.sh'
          }
        }

      }
    }

    stage('Load') {
      parallel {
        stage('Load') {
          steps {
            sh 'echo "Running Load Tasks"'
          }
        }

        stage('LoadPostgres1') {
          steps {
            sh 'sh /opt/jenkins_scripts/load1.sh'
          }
        }

        stage('LoadPostgres2') {
          steps {
            sh 'sh /opt/jenkins_scripts/load2.sh'
          }
        }

        stage('LoadPostgres3') {
          steps {
            sh 'sh /opt/jenkins_scripts/load3.sh'
          }
        }

      }
    }

    stage('Notify') {
      environment {
        Notify = ''
      }
      steps {
        sh '''echo "ETL stages have been successfully executed and data has been moved from Oracle to PostgreSQL."
'''
      }
    }

  }
}