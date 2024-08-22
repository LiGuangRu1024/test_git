# @time     ：2024/8/12 11:19
# @author   : 莉光哈哈哈
# @file     : test59_blockchain_development.py
# @software : PyCharm
'''
区块链开发
'''
import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8').hexdigest())


def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))


def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)


# 创建区块链并添加创世区块
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# 添加几笔交易
num_block_to_add = 10
for i in range(0, num_block_to_add):
    new_block_data = "Hey U Block #" + str(i)
    new_block = create_new_block(previous_block, new_block_data)
    blockchain.append(new_block)
    previous_block = new_block
    print("Block #{} has been added to the blockchain!".format(new_block.index))
    print("Hash: {}\n".format(new_block.hash))

'''
智能合约编写
'''


# 假设有一个简单的智能合约用于转移代币
class TokenContract:
    def __init__(self):
        self.balance = {}

    def transfer(self, sender, receiver, amount):
        if sender not in self.balance:
            self.balance[sender] = 0

        if receiver not in self.balance:
            self.balance[receiver] = 0

        if self.balance[sender] >= amount:
            self.balance[sender] -= amount
            self.balance[receiver] += amount
            return True
        return False


# 测试智能合约
contract = TokenContract()
contract.transfer("Alice", "Bob", 100)
print(contract.balance)  # 应该显示Alice和Bob的余额

'''
区块链数据分析
'''
import pandas as pd
import matplotlib.pyplot as plt

# 从区块链获取数据
# 假设data.csv包含了每个区块的交易数量
data = pd.read_csv("data.csv")

# 数据可视化
plt.figure(figsize=(10, 5))
plt.plot(data["index"], data["transactions"], marker="o")
plt.title("Transactions per Block Over Time")
plt.xlabel("Block Index")
plt.ylabel("Number of Transactions")
plt.show()

'''
区块链安全分析
'''
import hashlib
import time


def check_double_spend(blockchain):
    for i in range(1, len(blockchain)):
        if blockchain[i].previous_hash != blockchain[i - 1].hash:
            print(f"Double spend detected at block {i}!")
            break


# 使用前面创建的区块链
check_double_spend(blockchain)
