FROM jenkins/jenkins:lts-jdk11
ENV JAVA_OPTS=-Djenkins.install.runSetupWizard=false

USER jenkins

ARG cask_config
ARG jenkins_home
ARG jenkins_java_opts

ENV CASK_JENKINS_CONFIG=${cask_jenkins_config}
ENV JENKINS_HOME=${jenkins_home}
ENV JAVA_OPTS=${jenkins_java_opts}

USER jenkins


# Why each plugin is needed:
# plain-credentials is recommended in the github pull request builder's configuration page as the preferred method
# of providing your credentials to Jenkins.
# ghprb is to manage communication with github
# configuration-as-code is to allow jenkins elements to be configured with the yaml file format provided by the "Jenkins
# Configuration As Code" plugin
RUN jenkins-plugin-cli --plugins plain-credentials:1.7 ghprb:1.42.2 configuration-as-code:1.52
