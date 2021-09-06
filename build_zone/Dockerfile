FROM jenkins/jenkins:lts-jdk11
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false
ENV JAVA_HOME=/var/jenkins_home

USER jenkins
RUN jenkins-plugin-cli --plugins ghprb:1.42.2

