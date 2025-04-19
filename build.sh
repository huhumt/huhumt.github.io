#!/usr/bin/env bash

# bundle exec jekyll serve
bundle install && bundle exec jekyll build
# bundle exec jekyll serve --livereload

cp -r ./_site/* ../huhumt.bitbucket.io/
