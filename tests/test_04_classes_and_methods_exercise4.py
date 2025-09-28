def run(module):
    a1 = module.BankAccount("Alice", 100.0)
    a2 = module.BankAccount("Bob", 50.0)

    a1.deposit(50)
    assert a1.balance == 150.0, f"Deposit did not add funds properly"

    a1.withdraw(30)
    assert a1.balance == 120.0, f"Withdraw did not remove funds properly"

    a1.withdraw(1000)  # should fail silently
    assert a1.balance == 120.0, f"Withdraw did not fail silently when removing too much money"

    a1.transfer(a2, 20)
    assert a1.balance == 100.0, f"Transfer did not remove funds properly"
    assert a2.balance == 70.0, f"Received did not add funds properly"

    hist1 = a1.history()
    hist2 = a2.history()

    assert "Deposited 50" in hist1, "Deposit history does not match expected"
    assert "Withdrew 30" in hist1, "Withdraw history does not match expected"
    assert "Transferred 20 to Bob" in hist1, "Transfer history does not match expected"
    assert "Received 20 from Alice" in hist2, "Received history does not match expected"
