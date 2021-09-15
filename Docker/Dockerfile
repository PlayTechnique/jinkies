FROM jenkins/jenkins:lts-jdk11

ARG casc_jenkins_config
ARG jenkins_home
ARG jenkins_java_opts

ENV CASC_JENKINS_CONFIG=${casc_jenkins_config}
ENV JENKINS_HOME=${jenkins_home}
ENV JAVA_OPTS=${jenkins_java_opts}

# https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/docs/features/secrets.adoc#docker-secrets
USER root

RUN mkdir /run/secrets/ && chown jenkins:jenkins /run/secrets/ && chmod 0700 /run/secrets \
    && mkdir ${CASC_JENKINS_CONFIG} && chown jenkins:jenkins ${CASC_JENKINS_CONFIG}

USER jenkins


# Why each plugin is needed:
#
# plain-credentials is recommended in the github pull request builder's configuration page as the preferred method
# of providing your credentials to Jenkins.
# ghprb is to manage communication with github
# configuration-as-code is to allow jenkins elements to be configured with the yaml file format provided by the "Jenkins
# Configuration As Code" plugin
RUN jenkins-plugin-cli --plugins plain-credentials:1.7 ghprb:1.42.2 configuration-as-code:1.52

ADD secrets/ /run/secrets/
ADD jcasc/ ${CASC_JENKINS_CONFIG}/