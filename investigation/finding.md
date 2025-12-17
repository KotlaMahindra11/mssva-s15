
## Challenge 1 (CH1) - Authentication Bypass

**Challenge ID:** CH1  
**Target URL:** http://127.0.0.1:8001  
****Finding Summary:**** Authentication bypass vulnerability in login endpoint. The application accepts JSON requests with only a username field (no password), returning an "internal-access" token. This allows attackers to bypass authentication entirely.  
****Detection Method:**** Custom Nuclei template that sends a POST request with only username in JSON body  
****Template File:**** [ch1-auth-bypass.yaml](templates/ch1-auth-bypass.yaml)

### **Vulnerability Details**
•⁠  ⁠Endpoint: ⁠ /login ⁠ (POST)
•⁠  ⁠Vulnerability Type: Broken Authentication
•⁠  ⁠Severity: Critical
•⁠  ⁠Root Cause: Missing validation for required password field
****

## Challenge 2 (CH2) - Path Traversal

****Challenge ID:**** CH2  
****Target URL:**** http://127.0.0.1:8002  
****Finding Summary:**** Path traversal vulnerability in file download endpoint. The application uses ⁠ os.path.normpath() ⁠ which can be bypassed with certain encoding techniques to access files outside the intended directory.  
****Detection Method:**** Custom Nuclei template testing various path traversal payloads  
****Template File:**** [ch2-path-traversal.yaml](templates/ch2-path-traversal.yaml)

### Vulnerability Details
•⁠  ⁠*Endpoint:* ⁠ /download?file= ⁠
•⁠  ⁠*Vulnerability Type:* Local File Inclusion / Path Traversal
•⁠  ⁠*Severity:* High
•⁠  ⁠*Root Cause:* Insufficient path sanitization
****

