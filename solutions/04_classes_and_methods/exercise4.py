
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.ledger = []

    def deposit(self, amount: float):
        # TODO: 
        # - Only allow positive deposits
        # - Increase balance
        # - Add "Deposited X" to ledger
        if amount > 0:
            self.ledger.append(f"Deposited {amount}")
            self.balance += amount

    def withdraw(self, amount: float):
        # TODO:
        # - Only allow if amount <= balance and amount > 0
        # - Decrease balance
        # - Add "Withdrew X" to ledger
        # - If insufficient funds, do nothing
        if amount > 0 and amount <= self.balance:
            self.ledger.append(f"Withdrew {amount}")
            self.balance -= amount

    def transfer(self, other_account: "BankAccount", amount: float):
        # TODO:
        # - Withdraw from self, deposit into other_account
        # - Add "Transferred X to <other>" to self ledger
        # - Add "Received X from <self>" to other ledger
        # NOTE: Use the deposit and withdraw methods! Complete the transfer, THEN record this transfer and received history
        self.withdraw(amount)
        other_account.deposit(amount)
        self.ledger.append(f"Transferred {amount} to {other_account.owner}")
        other_account.ledger.append(f"Received {amount} from {self.owner}")

    def history(self) -> list[str]:
        # TODO: return the transaction ledger
        return self.ledger
