Note: This requires HandbrakeCLI

Readmore about HandbrakeCLI here:
https://handbrake.fr/docs/en/latest/cli/cli-options.html

A simple automatic downscaler that can be used for Davinci Resolve proxy or downscaled backups

Copy config.yml.dist to config.yml and edit it according to your needs

downscale.py:
   # Will scan the files from the source folder
   # Then check if it exists on the target folder
   # If it doesn't exist, downscale it using Handbrake
   # If it exists, skip