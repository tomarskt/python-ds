FROM ubuntu:20.04

MAINTAINER Sudhir Tomar

USER root

# RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN export LANGUAGE="en_US.UTF-8"
RUN export LANG="en_US.UTF-8"
RUN export LC_ALL="en_US.UTF-8"

RUN apt-get update && apt-get install -y gcc make curl wget
RUN apt-get update && apt-get install -y autoconf bison build-essential libssl-dev libyaml-dev libreadline-dev zlib1g-dev libncurses-dev libffi-dev libgdbm-dev

RUN apt-get update && apt-get install -y git
RUN git --version


# # # Install rbenv
RUN git clone https://github.com/rbenv/rbenv.git /usr/local/rbenv
RUN echo '# rbenv setup' > /etc/profile.d/rbenv.sh
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh
RUN chmod +x /etc/profile.d/rbenv.sh

# # # install ruby-build
RUN mkdir /usr/local/rbenv/plugins
RUN git clone https://github.com/rbenv/ruby-build.git /usr/local/rbenv/plugins/ruby-build

ENV RBENV_ROOT /usr/local/rbenv
ENV PATH $RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN rbenv install 2.6.0
RUN rbenv global 2.6.0
RUN ruby -v

COPY build.sh build.sh
RUN chmod 777 build.sh

RUN chmod 777 buildScripts/buildPlay.sh
RUN ./buildScripts/buildPlay.sh android stsh
