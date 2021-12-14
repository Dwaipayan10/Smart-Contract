print ("Hello World!")
import time
import json
import web3
from eth_account import Account
from web3.auto import w3
from web3.providers.websocket import WebsocketProvider
from web3 import Web3
from solc import compile_standard
with open("Contract.sol") as c:
 contractText=c.read()
with open(".pk") as pkfile:
 privateKey=pkfile.read()
with open(".infura") as infurafile:
 infuraKey=infurafile.read()
# Solidity source code
compiled_sol = compile_standard({
     "language": "Solidity",
     "sources": {
         "Greeter.sol": {
             "content": contractText
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
})
