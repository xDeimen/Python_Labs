class Blockchain:
    # Restul codului din exercițiul anterior

    def get_unmined_transactions(self):
        unmined_transactions = []
        for block in self.chain:
            unmined_transactions.extend(block['transactions'])
        return unmined_transactions

    def find_unmined_transactions(self):
        unmined_transactions = self.get_unmined_transactions()
        unmined_transactions_ids = set()
        for block in self.chain:
            for transaction in block['transactions']:
                unmined_transactions_ids.add(transaction['id'])
        return [transaction for transaction in unmined_transactions if transaction['id'] not in unmined_transactions_ids]

    def mine_transactions(self):
        unmined_transactions = self.find_unmined_transactions()
        if not unmined_transactions:
            print("Nu există tranzacții neîncăminate.")
            return

        previous_block = self.get_previous_block()
        previous_proof = previous_block['proof']
        proof = self.proof_of_work(previous_proof)
        previous_hash = self.hash(previous_block)
        self.create_block(proof, previous_hash)

        print("Tranzacțiile următoare au fost minate:")
        for transaction in unmined_transactions:
            print(transaction)

# Exemplu de utilizare:
blockchain = Blockchain()
blockchain.add_transaction("Alice", "Bob", 1.5)
blockchain.add_transaction("Charlie", "Dave", 3.2)
blockchain.add_transaction("Eve", "Frank", 2.7)

# Minează tranzacțiile neîncătimate
blockchain.mine_transactions()