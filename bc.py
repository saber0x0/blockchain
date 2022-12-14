#!/usr/bin/env python3
# coding=utf-8

import hashlib as hasher
import datetime as date

#每个区块的哈希值都是该区块索引、时间戳、数据和前一个区块哈希值的加密哈希值。数据可以是任何你想要的。
class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index                  # 区块索引
    self.timestamp = timestamp          # 时间戳
    self.data = data                    # 数据
    self.previous_hash = previous_hash  # 前一个区块hash值
    self.hash = self.hash_block()       # 前一个区块的hash值得加密hash值   
   
  def hash_block(self):                 # hash加密
    sha = hasher.sha256()
    sha.update(str(self.index).encode() + 
               str(self.timestamp).encode() + 
               str(self.data).encode() + 
               str(self.previous_hash).encode())
    return sha.hexdigest()      

def create_genesis_block():             #初始块 0号块
    # index zero and arbitrary previous hash
    return Block(0, date.datetime.now(), "hua's Block", "0")

def next_block(last_block):            # 1~∞ 链块
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm block " + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)   #返回新区块


if __name__=="__main__":
    # Create the blockchain and add the genesis block
    # 0号初始
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    # How many blocks should we add to the chain
    # after the genesis block
    # 添加20块
    num_of_blocks_to_add = 20

# Add blocks to the chain
    for i in range(0, num_of_blocks_to_add):           #20块
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add        
        # Tell everyone about it!
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash)) 

