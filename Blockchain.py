import hashlib
class NeuralcoinBlock:
    def __init__(self,previous_block_hash, transaction_list ):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna Send 2 BTC to Mike"
t2 = "Bob Send 4.2 BTC to Mike"
t3 = "Mike Send 2 BTC to Bob"
t4 = "Daniel Send 3.1 BTC to Anna"
t5 = "Mike Send 4.1 BTC to Charlie"
t6 = "Mike Send 2 BTC to Daniel"

initial_block = NeuralcoinBlock("Initial string",[t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralcoinBlock(initial_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralcoinBlock(initial_block.block_hash,[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)