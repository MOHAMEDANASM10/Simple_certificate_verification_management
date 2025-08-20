# 🎓 Academic Certificates on Blockchain  
_A simple blockchain system to issue, store, and verify academic certificates securely._  

---

## 🚀 Project Overview  
Fake certificates are a real problem today. Employers waste time verifying, students face fraud risks, and universities need a tamper-proof system.  

This project solves that problem by putting **academic certificates on a blockchain**.  
- **Universities** issue certificates → stored as blockchain records.  
- **Blockchain** makes records tamper-proof.  
- **Employers** instantly verify a student’s certificate by querying the blockchain.  

✅ **No fakes. No manual verification. 100% trust.**  

---

## 🔑 Key Features  
- **Genesis Block** → starts the blockchain.  
- **University Authorization** → only trusted universities can issue certificates.  
- **Certificate Mining** → new records are mined with proof-of-work.  
- **Employer Verification** → query student name to check authenticity.  
- **Immutable Ledger** → once a certificate is added, it can’t be altered.  

---

## 🛠️ How It Works (in simple steps)  

### 1️⃣ University Issues a Certificate  
```txt
> Add certificate record
Enter University ID: U001
Student Name: Moham
Course: B.Tech Computer Science
Year: 2025
👉 Certificate gets added to pending transactions.

2️⃣ Mining the Block

> Mine block
Enter University ID: U001
✅ Block mined: 000f3b12e…
🎓 Block validated by Oxford University

👉 Pending certificates are locked into blockchain with a hash.

3️⃣ Employer Verifies a Student
> Verify certificate
Enter Student Name: Moham
🎓 Certificates found for Moham:
{
  "student_name": "Moham",
  "course": "B.Tech Computer Science",
  "institution": "Oxford University",
  "year": "2025"
}

👉 Employer instantly knows it’s genuine.

🖥️ How to Run in VS Code

Save file as edu_blockchain.py.

Open VS Code → Terminal → run:
python edu_blockchain.py

Use the menu options:

1 → Add certificate (University only)

2 → Mine block (validate records)

3 → Show blockchain

4 → Validate blockchain integrity

5 → Employer verifies a student by name

6 → Exit

📊 Why This Project is Needed

🎓 Students → Protect their hard-earned degrees from fraud.

🏢 Employers → Instantly verify authenticity without contacting universities.

🏫 Universities → Prove they issued the certificate, no one else can fake it.

👉 In short: Transparency, Security, Trust.

🌟 Future Enhancements

🔐 Add dynamic university registration by admin.

📑 Auto-generate University IDs.

🌍 Web-based interface for public access.

📲 Mobile app for real-time verification.

🏆 Project Value

This is not just a “blockchain demo”.
It’s a practical solution that can save:

Time ⏳ (instant verification)

Money 💰 (no third-party verification agencies)

Reputation 🔒 (no fake degrees floating around)

✍️ Built with ❤️ to prove that blockchain isn’t just about Bitcoin — it can secure your education too.
