# Lessons Learned: Automating Syslog with Python and Rsyslog

## Overview
This project reinforced key concepts in centralized logging and automation:

### 1. Python Syslog Sender
- Reading logs from a file and sending them at controlled intervals improves reliability.
- Supporting both TCP and UDP ensures flexibility for different environments.

### 2. Rsyslog Filtering
- Custom rulesets allow precise control over which messages are logged.
- Using severity and hostname filters reduces noise and focuses on critical events.

### 3. Omprog Integration
- Triggering scripts based on log conditions enables automated responses.
- This approach can be extended to alerting or remediation workflows.

## Best Practices
- Validate inputs (protocol, file paths) to avoid runtime errors.
- Test configurations incrementally (start with UDP, then add TCP).
- Secure syslog traffic when crossing untrusted networks.

## Outcome
Combining Python scripting with Rsyslog configurations provides a powerful foundation for SIEM pipelines and automated incident handling.
