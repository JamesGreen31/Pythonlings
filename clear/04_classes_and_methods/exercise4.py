# REMOVE THIS TO MOVE ON

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        # TODO: store owner, balance, and an empty transaction history
        pass

    def deposit(self, amount: float):
        # TODO: 
        # - Only allow positive deposits
        # - Increase balance
        # - Add "Deposited X" to history
        pass

    def withdraw(self, amount: float):
        # TODO:
        # - Only allow if amount <= balance and amount > 0
        # - Decrease balance
        # - Add "Withdrew X" to history
        # - If insufficient funds, do nothing
        pass

    def transfer(self, other_account: "BankAccount", amount: float):
        # TODO:
        # - Withdraw from self, deposit into other_account
        # - Add "Transferred X to <other>" to self history
        # - Add "Received X from <self>" to other history
        # NOTE: Use the deposit and withdraw methods! Complete the transfer, THEN record this transfer and received history
        pass

    def history(self) -> list[str]:
        # TODO: return the transaction history
        return None
