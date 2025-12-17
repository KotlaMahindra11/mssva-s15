
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


**Target URL:** http://172.16.13.89:9005  
**Finding Summary:** Session management misconfiguration identified through black-box analysis. The application may have issues with session token validation, predictable session IDs, or improper cookie security flags.  
**Detection Method:** Custom Nuclei template analyzing session handling and cookie manipulation  
**Template File:** [ch5-session-misconfiguration.yaml](templates/ch5-session-misconfiguration.yaml)

### Vulnerability Details
- **Vulnerability Type:** Session Management Flaw
- **Testing Model:** Black-box
- **Severity:** Medium to High
- **Potential Issues:** Missing HttpOnly/Secure flags, session fixation, weak session tokens

---

## Challenge 6 (CH6) - State Desync

**Challenge ID:** CH6  
**Target URL:** http://127.0.0.1:9020  
**Finding Summary:** State desynchronization vulnerability in multi-stage workflow. The application allows skipping required stages (stage 2) and directly committing, resulting in unintended "extended" mode access with additional operations. This is a logic flaw where mandatory steps can be bypassed.  
**Detection Method:** Custom Nuclei template that performs /init then directly calls /commit, skipping /advance  
**Template File:** [ch6-state-desync.yaml](templates/ch6-state-desync.yaml)

### Vulnerability Details
- **Endpoints:** `/init`, `/advance`, `/commit`
- **Vulnerability Type:** Business Logic Flaw / State Desync
- **Severity:** High
- **Root Cause:** Stage 2 advancement is not enforced before commit

---

## Challenge 7 (CH7) - Access Control Bypass

**Challenge ID:** CH7  
**Target URL:** http://172.16.13.89:9021  
**Finding Summary:** Access control bypass through header injection. The application trusts client-supplied headers for determining access rights or client IP, allowing attackers to bypass restrictions by injecting headers like X-Forwarded-For, X-Real-IP, or similar.  
**Detection Method:** Custom Nuclei template testing various trust-related HTTP headers  
**Template File:** [ch7-access-control.yaml](templates/ch7-access-control.yaml)

 Vulnerability Details
- Vulnerability Type: Broken Access Control / Header Injection
- Testing Model: Black-box
- Severity: Critical
- Potential Impact: Authentication bypass, privilege escalation, access to restricted resources

---

