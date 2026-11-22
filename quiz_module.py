import sys
import time


QUESTIONS = [
    {
        "id": 1,
        "category": "Phishing Email - Lookalike Domain",
        "scenario": (
            "You receive an email appearing to come from 'CodeAlpha Support <support@codealpha-verify-portal.com>' "
            "asking you to log in within 2 hours to confirm your task submission."
        ),
        "options": [
            "A) Click the link and enter credentials quickly so your submission isn't missed",
            "B) Check the actual domain/official portal independently and avoid logging in via the suspicious link",
            "C) Reply with your password so support can verify your account manually"
        ],
        "answer": "B",
        "explanation": (
            "Attackers register lookalike or hyphenated domains ('codealpha-verify-portal.com') and add artificial "
            "time pressure ('2 hours') to harvest credentials. Always verify via official channels directly."
        ),
    },
    {
        "id": 2,
        "category": "Social Engineering - MFA Fatigue",
        "scenario": (
            "At 1:15 AM, your phone gets 5 consecutive MFA approval pop-ups for an account you are not trying to "
            "access right now."
        ),
        "options": [
            "A) Tap Approve once so the notifications stop",
            "B) Turn off your phone and ignore it until next week",
            "C) Tap Deny, change your password immediately, and check active sessions/2FA settings"
        ],
        "answer": "C",
        "explanation": (
            "Repeated unsolicited prompts are classic MFA fatigue (push bombing). Approving even once can grant "
            "an attacker access; always deny, rotate credentials, and audit sessions."
        ),
    },
    {
        "id": 3,
        "category": "Social Engineering - Pretexting & Impersonation",
        "scenario": (
            "Someone messages claiming to be from 'IT / Placement Desk' asking for your one-time verification code "
            "to fix a 'sync error' on your student/intern profile."
        ),
        "options": [
            "A) Share the OTP since they claimed an internal technical issue",
            "B) Refuse to share codes and verify the request through an official, trusted contact channel",
            "C) Send your account recovery backup codes instead"
        ],
        "answer": "B",
        "explanation": (
            "Legitimate support/administrators do not ask for your OTP or recovery codes. Pretexting uses a plausible "
            "technical excuse to bypass authentication."
        ),
    },
    {
        "id": 4,
        "category": "Fake Website - Credential Harvesting",
        "scenario": (
            "A link leads to a page that looks almost identical to a login screen, has a slightly off URL, and "
            "shows an error when you type a wrong password—then asks again."
        ),
        "options": [
            "A) Treat it as a potential credential-harvesting page, close it, and report the URL",
            "B) Try a backup password to see if that one goes through",
            "C) Disable browser security warnings to continue"
        ],
        "answer": "A",
        "explanation": (
            "Fake login pages often mimic real UIs and loop or show generic errors to capture passwords. Never enter "
            "real credentials on unverified domains."
        ),
    },
    {
        "id": 5,
        "category": "Social Engineering - Baiting & Malicious Attachment",
        "scenario": (
            "An unexpected email with a vague greeting sends 'Exam_Schedule_Update.zip' and says to extract and "
            "run the file inside for details."
        ),
        "options": [
            "A) Extract and run whatever file is inside immediately",
            "B) Do not run unexpected executables/scripts from untrusted attachments; verify via official notice",
            "C) Forward it to classmates/colleagues to see if it works for them"
        ],
        "answer": "B",
        "explanation": (
            "Unexpected archives/attachments are common malware delivery bait. Verify announcements on official "
            "portals rather than running unsolicited files."
        ),
    },
    {
        "id": 6,
        "category": "Phishing - Urgency & Fear Hooks",
        "scenario": (
            "A message warns: 'FINAL NOTICE: Your account will be permanently deleted in 30 minutes unless you "
            "click here and pay a small reactivation fee.'"
        ),
        "options": [
            "A) Panic-click and pay immediately to save the account",
            "B) Pause—extreme urgency plus payment/link demands is a classic phishing red flag; verify independently",
            "C) Save your card details in the form for faster future payments"
        ],
        "answer": "B",
        "explanation": (
            "Manufactured panic ('30 minutes', 'permanently deleted') combined with links or payments is designed to "
            "override critical thinking."
        ),
    },
    {
        "id": 7,
        "category": "Defense & Best Practices",
        "scenario": (
            "Which habit best protects your accounts even if a password is leaked or a lookalike site is visited?"
        ),
        "options": [
            "A) Reusing the same strong password across all accounts",
            "B) Using unique passwords per account plus strong 2FA/passkeys",
            "C) Keeping passwords written in a plain text file on your desktop"
        ],
        "answer": "B",
        "explanation": (
            "Unique passwords contain breach blast radius, and strong 2FA/passkeys add a second verification factor "
            "beyond just a password."
        ),
    },
    {
        "id": 8,
        "category": "Fake Website - Typosquatting",
        "scenario": (
            "You see 'g00gle-security-check.com' or 'lnkedin-login.com' in a message. What is this technique called?"
        ),
        "options": [
            "A) Typosquatting / lookalike domain spoofing",
            "B) DNSSEC validation",
            "C) End-to-end encryption"
        ],
        "answer": "A",
        "explanation": (
            "Typosquatting / lookalike domains use character swaps, misspellings, or extra words to trick users into "
            "trusting a fraudulent domain."
        ),
    },
]


def run_quiz():
    print("=" * 64)
    print("   PHISHING AWARENESS & SOCIAL ENGINEERING - INTERACTIVE QUIZ")
    print("=" * 64)
    print(f"Total Scenarios: {len(QUESTIONS)} | Type A, B, or C and press Enter.\n")

    score = 0
    missed = []

    for q in QUESTIONS:
        print(f"--- Question {q['id']}/{len(QUESTIONS)} [{q['category']}] ---")
        print(q["scenario"])
        print()
        for opt in q["options"]:
            print(f"  {opt}")
        print()

        while True:
            choice = input("Your choice (A/B/C): ").strip().upper()
            if choice in ("A", "B", "C"):
                break
            print("Please enter A, B, or C.")

        if choice == q["answer"]:
            score += 1
            print("\n[CORRECT] Nice spot.")
        else:
            missed.append((q, choice))
            print(f"\n[INCORRECT] Expected {q['answer']}.")

        print(f"Why: {q['explanation']}\n")
        time.sleep(0.2)

    accuracy = (score / len(QUESTIONS)) * 100
    print("=" * 64)
    print("                        QUIZ SUMMARY")
    print("=" * 64)
    print(f"Final Score : {score} / {len(QUESTIONS)} ({accuracy:.1f}%)")

    if score == len(QUESTIONS):
        print("Rating      : Strong phishing & social engineering awareness.")
    elif score >= 6:
        print("Rating      : Good baseline—review missed scenarios to tighten instincts.")
    else:
        print("Rating      : Needs review—read TRAINING_GUIDE.md and retake the quiz.")

    if missed:
        print("\nAreas to Review:")
        for q, user_ans in missed:
            print(f"  - Q{q['id']} ({q['category']}): You picked {user_ans}, answer was {q['answer']}")

    print("=" * 64)


if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz exited.")
        sys.exit(0)