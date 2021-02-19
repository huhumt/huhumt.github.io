#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "huhumt/huhumt.github.io@main"
}

# site config
site_name = "my site"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "TinyFish"
email = "nepood@gmail.com"
author_homepage = "https://huhumt.github.io"
description = "no silence"
key_words = ['github', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "homepage",
        "url": "https://huhumt.github.io",
        "brief": "keep going"
    },
    {
        "name": "repo",
        "url": "https://github.com/huhumt",
        "brief": "keep going"
    },
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archive",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/huhumt",
        "icon": "gi gi-github"
    },
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
