FROM ubuntu:16.04

MAINTAINER Sudhir Tomar

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN  apt-get update
RUN  apt-get install -y --force-yes autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev
RUN  apt-get install -y --force-yes build-essential curl git
RUN apt-get install -y -q git
RUN apt-get install -y libssl-dev

# Install rbenv
RUN git clone https://github.com/rbenv/rbenv.git /usr/local/rbenv
RUN echo '# rbenv setup' > /etc/profile.d/rbenv.sh
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh
RUN echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh
RUN chmod +x /etc/profile.d/rbenv.sh


#RUN git clone https://github.com/rbenv/rbenv.git ~/.rbenv
#RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
#RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc
RUN source ~/.bashrc
#RUN bash -c 'rbenv -v'
#RUN bash -c 'rbenv install $RUBY_VERSION'
#RUN type rbenv

# install ruby-build
RUN mkdir /usr/local/rbenv/plugins
RUN git clone https://github.com/rbenv/ruby-build.git /usr/local/rbenv/plugins/ruby-build

ENV RBENV_ROOT /usr/local/rbenv

ENV PATH $RBENV_ROOT/bin:$RBENV_ROOT/shims:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

ENV RUBY_VERSION 2.6.0
RUN rbenv install $RUBY_VERSION && rbenv local $RUBY_VERSION
RUN rbenv global $RUBY_VERSION

RUN echo "gem: --no-document" > ~/.gemrc

RUN gem install bundler

ENV RUBYGEMS_VERSION 2.6.10

RUN gem install fastlane -NV \
  && gem install fastlane-plugin-appicon fastlane-plugin-android_change_string_app_name fastlane-plugin-humanable_build_number \
  && gem update --system "$RUBYGEMS_VERSION"

RUN fastlane -v && ruby -v && bundler -v && rbenv -v
