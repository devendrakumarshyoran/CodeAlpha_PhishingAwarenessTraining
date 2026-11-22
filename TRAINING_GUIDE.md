# Phishing Awareness & Social Engineering Defense Guide

## 1. Overview
Phishing and social engineering attacks exploit human trust, urgency, and routine habits rather than just software vulnerabilities. Recognizing manipulation patterns and verifying requests out-of-band stops most attacks before credentials or access are compromised.

## 2. Phishing Emails & Fake Websites
### Phishing Email Indicators
- **Lookalike / Spoofed Domains:** Subtle character changes or extra subdomains (e.g., `supp0rt-codealpha.com`, `login.university-portal-verify.in`, or homoglyphs). Always inspect the actual sender address and full domain, not just the display name.
- **Urgency, Fear, or Greed Hooks:** Threats of account suspension within hours, legal/fee penalties, or "limited-time" stipend/reward claims designed to rush hasty clicks.
- **Generic Greetings & Mismatched Links:** Vague openings (`Dear Student/User`) paired with anchor text that points to an unrelated URL on hover/inspection.
- **Risky Attachments:** Unexpected `.zip`, `.iso`, `.lnk`, `.hta`, `.xlsm`, or macro/script files claiming to be invoices, offer updates, or task sheets.

### Fake Websites & Credential Harvesters
- **Cloned Login Portals:** Pages mimicking email, banking, university, or developer portals hosted on unfamiliar domains or free/temporary subdomains.
- **Credential & Session Harvesting:** Prompts asking you to re-enter passwords, OTPs, or recovery codes after clicking an external link.
- **Missing/Misleading Trust Cues:** Unfamiliar URLs, typos in branding, broken secondary pages, or unexpected redirects after login.

## 3. Social Engineering Tactics
- **Pretexting:** Fabricating a believable scenario or back-story (e.g., IT helpdesk audit, placement/internship verification, or billing issue) to extract information or action.
- **Impersonation / Authority Abuse:** Pretending to be a manager, professor, HR/coordinator, bank official, or support agent to pressure compliance.
- **Baiting:** Offering something attractive—free software, cracked tools, urgent files, or rewards—to lure users into opening malicious links or files.
- **MFA Fatigue (Push Bombing):** Sending repeated multi-factor authentication push prompts (often late at night or during busy hours) hoping the user taps "Approve" just to stop notifications.

## 4. Real-World Scenarios
1. **Fake Internship / Stipend Verification Email:** An email with a lookalike domain claims your internship record or stipend release requires immediate login via a provided link. *Red flag:* Unexpected external link + artificial deadline; verify directly via official channels.
2. **Urgent Security / Account Lockout Alert:** A message warns of "unusual sign-in activity" and threatens permanent deactivation unless you verify credentials immediately. *Red flag:* Fear/urgency hook; open the official site/app directly instead of clicking email links.
3. **MFA Push Bombing:** You receive 6+ login approval prompts on your authenticator app without initiating a sign-in. *Red flag:* Unsolicited MFA request; **Deny** all prompts, change your password, and revoke active sessions.
4. **Malicious "Syllabus / Invoice" Archive:** A message attaches a password-protected `.zip` or `.iso` file with instructions to extract and run a file inside. *Red flag:* Archive/executable payload and password protection used to bypass email scanners.

## 5. Defense & Best Practices
- **Verify Out-of-Band:** Never trust contact details or links inside a suspicious message; check official bookmarks or known contacts independently.
- **Inspect Domains Carefully:** Read the root domain right before the first `/` and check for misspellings or extra hyphens/words.
- **Use Strong Unique Passwords + Phishing-Resistant 2FA:** Pair a password manager with authenticator apps or hardware/passkey security keys; never approve unexpected MFA prompts.
- **Handle Attachments & Links Safely:** Scan or avoid unexpected executables/archives, and report suspicious emails/messages to security or administrators promptly.