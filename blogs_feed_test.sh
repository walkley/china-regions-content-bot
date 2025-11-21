#!/bin/bash

curl -s https://aws.amazon.com/blogs/aws/feed/ | \
  xmllint --xpath "//item/link/text()" - 2>/dev/null | \
  while read -r BLOG_URL; do
    echo "=============================================="
    ./validate.sh -u "$BLOG_URL" -r cn-northwest-1 -p cn
  done
