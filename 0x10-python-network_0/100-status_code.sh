#!/bin/bash
# displays only the status code of the response.
curl -sI -w "%{response_code}" -o /dev/null "$1"
