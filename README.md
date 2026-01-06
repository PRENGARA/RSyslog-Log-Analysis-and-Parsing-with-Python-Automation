# RSyslog-Log-Analysis-and-Parsing-with-Python-Automation
Requirements to send syslog via TCP or UDP from a Python script
# Rsyslog Automation Project — Syslog Sender & Custom Rules

This repository contains Priyadharshini Rengaramanujam's Rsyslog implementation:

## Tasks
1. **send_syslog.py** — Python function to send syslog messages from a file to a specified host via TCP or UDP.
2. **Custom Ruleset** — `<lastname>_rules.conf` to filter and log messages with severity Warning or higher from host `server1` into `/var/log/server1_important.log`.
3. **Omprog** — `<lastname>_omprog.conf` to trigger a Python script (`webserver_omprog.py`) when Emergency severity messages from `webserver` are detected.

## Deliverables
- `scripts/send_syslog.py` — Reads `system2.log` and sends messages at 1-second intervals.
- `configs/<lastname>_rules.conf` — Rsyslog ruleset for filtering important logs.
- `configs/<lastname>_omprog.conf` — Omprog configuration for executing Python script.
- `scripts/webserver_omprog.py` — Python script triggered by omprog.

## Key Requirements
- Support both TCP and UDP protocols.
- Validate protocol input; print error if invalid.
- Log format: timestamp | severity | hostname | tag | message.
- Omprog writes Emergency messages to `/var/log/omprog.log`.

## Author
**Priyadharshini Rengaramanujam**
