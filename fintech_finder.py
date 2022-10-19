# Streamlit as an Interface

#In this part of the activity you will import the functions from your crypto_wallet.py file and create an interface using streamlit
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Streamlit Code

# Create Streamlit application headings using `st.markdown` to explain this app is for buying kitties
st.markdown("# Fintech Finder")
st.markdown("## Sub-Heading")
st.text(" \n")

#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

#  Call the `get_balance` function and save it as the variable `ether`
ether = get_balance(w3,account.address)


# Disply the balance of ether in the account
st.sidebar.markdown("## Your Balance of Ether")
st.sidebar.markdown(ether)
st.sidebar.markdown("---------")