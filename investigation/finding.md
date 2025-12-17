## Challenge 1 (CH1) - Authentication Bypass

**Challenge ID:** CH1  
**Target URL:** http://127.0.0.1:8001  
Finding Summary: Authentication bypass vulnerability in login endpoint. The application accepts JSON requests with only a username field (no password), returning an "internal-access" token. This allows attackers to bypass authentication entirely.  
Detection Method: Custom Nuclei template that sends a POST request with only username in JSON body  
Template File: [ch1-auth-bypass.yaml](templates/ch1-auth-bypass.yaml)

Vulnerability Details
•⁠  ⁠Endpoint: ⁠ /login ⁠ (POST)
•⁠  ⁠Vulnerability Type: Broken Authentication
•⁠  ⁠Severity: Critical
•⁠  ⁠Root Cause: Missing validation for required password field


