import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # Creates a new Block and adds it to the chain
    pass

  def new_transaction(self):
    # Adds a new transaction to the list of transactions
    pass

  @staticmethod
  def hash(block):
    # Hashes a Block
    pass

  @property
  def last_block(self):
    # Returns the last Block in the chain
    pass

  def proof_of_work(self, last_proof):
    """
    Simple Proof of Work Algorithm:
      - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
      - p is the previous proof, and p' is the new proof
    :param last_proof: <int>
    :return: <int>
    """
    proof = 0
    while self.valid_proof(last_proof, proof) is False:
        proof += 1

    return proof

  @staticmethod
  def valid_proof(last_proof, proof):
    """
    Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :return: <bool> True if correct, False if not.
    """

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"