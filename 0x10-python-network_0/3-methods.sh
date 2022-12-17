#!/bin/bash
# Requests for methods from a URL
curl -ILs "$1" | grep Allow | cut -d " " -f2-
