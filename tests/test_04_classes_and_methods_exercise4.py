def run(module):
    a1 = module.BankAccount("Alice", 100.0)
    a2 = module.BankAccount("Bob", 50.0)

    a1.deposit(50)
    assert a1.balance == 150.0

    a1.withdraw(30)
    assert a1.balance == 120.0

    a1.withdraw(1000)  # should fail silently
    assert a1.balance == 120.0

    a1.transfer(a2, 20)
    assert a1.balance == 100.0
    assert a2.balance == 70.0

    hist1 = a1.history()
    hist2 = a2.history()

    assert "Deposited 50" in hist1
    assert "Withdrew 30" in hist1
    assert "Transferred 20 to Bob" in hist1
    assert "Received 20 from Alice" in hist2
