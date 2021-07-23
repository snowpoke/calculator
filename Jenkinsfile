pipeline {
	agent any
	triggers {
		pollSCM('* * * * *')
	}
	stages {
		stage("Code execution"){
			steps {
				sh "python calculator.py 3 5"
			}
		}
		stage("Unit test"){
			steps {
				sh "python ./test_calculator.py"
			}
		}
	}
}
