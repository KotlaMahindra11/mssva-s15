**FINDING 1**
Title: Authentication logic allows access without password
Flag: Design Assumption Broken
Location: nuclei-bootcamp/apps/ch1-auth/app.py
Trigger Condition: POST request to /login with username but without password
Root Cause: The authentication flow assumes that the presence of a username is sufficient for partial authentication and issues an access token without validating credentials.
Impact: Unauthorized users can obtain an access token without providing valid authentication credentials, breaking the intended security model.
Evidence: A POST request containing only a username returns a 200 OK response with a token (internal-access), demonstrating authentication bypass.
