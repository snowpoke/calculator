pipeline {
	agent any
	stages {
		stage("Compile") {
			steps {
				sh "./gradlew compileJava"
			}
		}
		stage("Unit Test") {
			steps {
				echo "Skipping Unit Tests"
			}
		}
	}
}
