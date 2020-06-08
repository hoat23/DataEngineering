FROM centos:7
MAINTAINER hoat23 <deiner.zapata@gmail.com>

USER root

ARG HADOOP_VERSION=2.7.7

#RUN yum clean all
#RUN yum -y update 

#install dev tools
RUN yum clean all; \
    rpm --rebuilddb; \
    yum install -y initscripts curl which tar sudo rsync openssh-server openssh-clients

RUN yum update -y libselinux

############## ssh setting ##############
ADD config/ssh-config /root/.ssh/config
RUN chmod 600 /root/.ssh/config
RUN chown root:root /root/.ssh/config

RUN echo "/usr/sbin/sshd" >> ~/.bashrc

# ssh without key
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN /usr/bin/ssh-keygen -A


##############    java    ##############
#RUN yum install java-11-openjdk-devel
RUN yum -y install java-1.8.0-openjdk-devel
RUN java -version
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk/
#ENV PATH $PATH:$JAVA_HOME/bin
#RUN rm /usr/bin/java && ln -s $JAVA_HOME/bin/java /usr/bin/java

##############   hadoop   ##############
RUN curl http://apache.tt.co.kr/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -o hadoop-$HADOOP_VERSION.tar.gz
RUN sudo tar -xvf /hadoop-$HADOOP_VERSION.tar.gz -C /usr/local
RUN cd /usr/local && ln -s ./hadoop-$HADOOP_VERSION hadoop
RUN cd /usr/local/hadoop && mkdir -p logs

ENV HADOOP_HOME=/usr/local/hadoop
ENV HADOOP_PREFIX /usr/local/hadoop
ENV HADOOP_COMMON_HOME /usr/local/hadoop
ENV HADOOP_HDFS_HOME /usr/local/hadoop
ENV HADOOP_MAPRED_HOME /usr/local/hadoop
ENV HADOOP_YARN_HOME /usr/local/hadoop
ENV HADOOP_CONF_DIR /usr/local/hadoop/etc/hadoop
ENV YARN_CONF_DIR $HADOOP_PREFIX/etc/hadoop

ENV PATH $PATH:$HADOOP_PREFIX/bin
ENV PATH $PATH:$HADOOP_PREFIX/sbin

ENV HOME /root

WORKDIR /root

EXPOSE 80

