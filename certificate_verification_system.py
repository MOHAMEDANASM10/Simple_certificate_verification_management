import hashlib
import time
import json


class Block:
    def __init__(self, index, timestamp, certificates, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.certificates = certificates
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'certificates': self.certificates,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"✅ Block mined: {self.hash}")


class CertificateBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_certificates = []
        self.mining_reward = "Verification Credit"

        # 🔐 Pre-registered trusted universities
        self.authorized_universities = {
            "U001": "Oxford University",
            "U002": "MIT",
            "U003": "IIT Madras",
            "U004": "Stanford University"
        }

    def create_genesis_block(self):
        return Block(0, time.time(), ["Genesis Block: Academic Certificates"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_certificates(self, university_id):
        if university_id not in self.authorized_universities:
            print("⛔ Unauthorized University ID. Cannot mine certificates.")
            self.pending_certificates = []  # clear fake attempts
            return

        # Add a reward transaction
        self.pending_certificates.append(
            {"issuer": "System", "to": university_id, "reward": self.mining_reward}
        )

        block = Block(len(self.chain), time.time(), self.pending_certificates, self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        self.chain.append(block)
        print(f"🎓 Block validated by {self.authorized_universities[university_id]}")
        self.pending_certificates = []  # reset

    def add_certificate(self, university_id, student_name, course, year):
        if university_id not in self.authorized_universities:
            print("⛔ Unauthorized attempt! Only registered universities can add certificates.")
            return

        institution = self.authorized_universities[university_id]
        self.pending_certificates.append({
            "student_name": student_name,
            "course": course,
            "institution": institution,
            "year": year
        })
        print(f"✅ Certificate added by {institution}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "certificates": block.certificates,
                "hash": block.hash,
                "previous_hash": block.previous_hash
            }, indent=4))
            print("-" * 40)

    # 🔍 Employer verification by student name
    def verify_certificate(self, student_name):
        found_records = []
        for block in self.chain:
            for cert in block.certificates:
                if isinstance(cert, dict) and cert.get("student_name") == student_name:
                    found_records.append(cert)

        if found_records:
            print(f"\n🎓 Certificates found for {student_name}:")
            for rec in found_records:
                print(json.dumps(rec, indent=4))
        else:
            print(f"\n⚠️ No certificate found for {student_name}. May be fake or not issued yet.")


# --- CLI Demo ---
if __name__ == "__main__":
    edu_chain = CertificateBlockchain()

    while True:
        print("\n=== Academic Certificates Blockchain with University Authorization ===")
        print("1. Add certificate record (University only)")
        print("2. Mine block (validate records)")
        print("3. Show blockchain")
        print("4. Validate blockchain")
        print("5. Verify certificate by student name (Employer Access)")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            uid = input("Enter University ID: ")
            student = input("Student Name: ")
            course = input("Course: ")
            year = input("Year: ")
            edu_chain.add_certificate(uid, student, course, year)

        elif choice == "2":
            uid = input("Enter University ID for validation: ")
            edu_chain.mine_pending_certificates(uid)

        elif choice == "3":
            edu_chain.print_chain()

        elif choice == "4":
            print("Blockchain valid?", edu_chain.is_chain_valid())

        elif choice == "5":
            student = input("Enter Student Name to verify: ")
            edu_chain.verify_certificate(student)

        elif choice == "6":
            break

        else:
            print("Invalid choice, try again.")
