##6

pipline  {
    agent any

    stages  {
        stage ('one') {
            steps {
                bat 'echo eli >> jen_file.txt'
            }
        }
        stage ('two') {
            steps {
                bat 'type jen_file.txt'
            }
        }
        stage ('three') {
            steps {
                bat 'fsutil volume diskfree c:'
            }
        }
        stage ('four') {
            steps {
                bat 'move jen_file.txt C:\users\1\Documents'
            }
        }
    }
}

##7

pipline {
agent any

    stages {
        stage ('test') {
            steps {
                dir ('c:\users\1\PycharmProjects\class5\venv\pipeline.py') {
                    bat 'pipeline.py'
                }
            }
        }
    }
}

