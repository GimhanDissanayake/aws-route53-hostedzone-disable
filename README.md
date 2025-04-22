# aws-route53-hostedzone-disable
Python script to disable a AWS Route53 Hosted Zone

# Intro
This script temporarily disable all the DNS records in a Hosted Zone by adding a prefix "disabled_". To re-enable any DNS record, you can simply edit it and remove the prefix "disabled_".

# How to use

1. Upload the main.py and list_records.py to cloudshell

2. Execute main.py
```
python3 main.py
```